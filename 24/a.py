from collections import deque
import copy

sign_to_path = {
    '>': (0, 1),
    '<': (0, -1),
    '^': (-1, 0),
    'v': (1, 0)
}

directions = [(0, 1), (0, -1), (-1, 0), (1, 0), (0, 0)]

with open('input', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

    grid = []

    blizzards = []

    # read the map twice, whatever
    for i, l in enumerate(lines):
        grid.append([])
        for j, c in enumerate(l):
            if c in ('>', '<', 'v', '^'):
                grid[i].append('.')
                blizzards.append(((i, j), sign_to_path[c]))
            else:
                grid[i].append(c)

def print_blizzards(blizzards):
    print()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) in [r[0] for r in blizzards]:
                print('x', end='')
            else:
                print(grid[i][j], end='')
        print()

def compute_next_blizzards(blizzards):
    res = []
    for b in blizzards:
        new_b = [b[0][0] + b[1][0], b[0][1] + b[1][1]]
        if grid[new_b[0]][new_b[1]] == '#':
            non_move_row = b[1].index(0)
            move_row = (non_move_row + 1) % 2

            if b[1][move_row] == 1:
                new_b[move_row] = 1
            else:
                new_b[move_row] = len(grid) - 2 if move_row == 0 else len(grid[0]) - 2

        res.append((tuple(new_b), b[1]))

    return res

time_to_blizzard = {
    0: blizzards #(blizzards, set([b[0] for b in blizzards]))
}

i = 0
curr_b = blizzards
while True:

    new_b = compute_next_blizzards(curr_b)

    if new_b in time_to_blizzard.values():
        break

    i += 1

    time_to_blizzard[i] = new_b
    curr_b = new_b

cycle_length = i + 1

print('cycle length', cycle_length)

time_to_blizzard_s = {
    k: set([b[0] for b in time_to_blizzard[k]])
    for k in time_to_blizzard
}

original_duration = 0

target = (len(grid) - 1, len(grid[0]) - 2)

q = deque([(original_duration, (0, 1))])

visited = set()

t = 0

while q:
    steps, pos = q.popleft()

    steps = steps + 1

    if (steps % cycle_length, pos) in visited:
        continue

    if pos == target:
        t += steps - original_duration - 1
        break

    b_set = time_to_blizzard_s[steps % cycle_length]

    visited.add((steps % cycle_length, pos))

    for d in directions:
        new_pos = (pos[0] + d[0], pos[1] + d[1])

        if new_pos[0] < 0 or new_pos[0] >= len(grid) or new_pos[1] < 0 or new_pos[1] >= len(grid[0]) or grid[new_pos[0]][new_pos[1]] == '#' or new_pos in b_set:
            continue

        q.append((steps, new_pos))

print(t)
