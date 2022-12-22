import re

with open('input_map', 'r') as fm:
    lines = [l.rstrip() for l in fm.readlines()]

    height = len(lines)
    width = max([len(l) for l in lines])

    grid = [[l[i] if i < len(l) else ' ' for i in range(width)] for l in lines]

with open('input', 'r') as f:
    exp = re.compile(r'([A-Z]|\d+)')
    r = exp.finditer(f.read())

    moves = [m.group(0) for m in r]

vals = {
    (0, 1): 0,
    (1, 0): 1,
    (0, -1): 2,
    (-1, 0): 3
}

# i increasing = R turn, i decreasing = L turn
# R, D, L, U
orientations = [(0, 1), (1, 0), (0, -1), (-1, 0)]
o = 0

# cannot be mithered to code this
# test input
# pos = (0, 8)

# real input
pos = (0, 50)

for move in moves:
    if move.isnumeric():
        for i in range(int(move)):
            # take a step
            np = (pos[0] + orientations[o][0], pos[1] + orientations[o][1])

            # if reach limit of map (== ' ' or max width or max height), 
            # traverse map from the other side until you meet a non-' ' square
            # if the first non-' ' thing you find is a wall, stay in original 
            # position, else keep moving
            if np[0] >= height or np[1] >= width or np[0] < 0 or np[1] < 0 or grid[np[0]][np[1]] == ' ':
                if orientations[o] == (1, 0):
                    temp = (0, pos[1])
                elif orientations[o] == (0, 1):
                    temp = (pos[0], 0)
                elif orientations[o] == (-1, 0):
                    temp = (height - 1, pos[1])
                else:
                    temp = (pos[0], width - 1)

                while grid[temp[0]][temp[1]] != '#' and grid[temp[0]][temp[1]] != '.':
                    temp = (temp[0] + orientations[o][0], temp[1] + orientations[o][1])

                if grid[temp[0]][temp[1]] == '#':
                    # not moving, break
                    break

                np = temp

            # if wall -> stop moving
            elif grid[np[0]][np[1]] == '#':
                break

            pos = np
    else:
        if move == 'R':
            o = (o + 1) % len(orientations)
        else:
            o = (o - 1) % len(orientations)

print(pos)
print(orientations[o])

res = 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + vals[orientations[o]]

print(res)