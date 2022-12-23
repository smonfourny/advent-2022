elf_positions = set()

with open('input', 'r') as f:
    for i, l in enumerate(f.readlines()):
        for j, c in enumerate(l):
            if c == '#':
                elf_positions.add((i, j))

directions = set([(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)])

decisions = [
    # to_check, move_to
    # north
    ([(-1, -1), (-1, 0), (-1, 1)], (-1, 0)),
    # south
    ([(1, -1), (1, 0), (1, 1)], (1, 0)),
    # west
    ([(-1, -1), (0, -1), (1, -1)], (0, -1)),
    # east
    ([(-1, 1), (0, 1), (1, 1)], (0, 1))
]

decision_index = 0

def print_map():
    ys = [p[0] for p in elf_positions]
    xs = [p[1] for p in elf_positions]

    max_x = max(xs)
    min_x = min(xs)
    max_y = max(ys)
    min_y = min(ys)

    for i in range(min_y - 1, max_y + 2):
        for j in range(min_x - 1, max_x + 2):
            if (i, j) in elf_positions:
                print('#', end='')
            else:
                print('.', end='')
        print()

c = 0

while True:
    c += 1

    print(f'round {c}')

    proposed_moves = {}

    invalid_moves = set()
    elves_sticking_around = set()

    moved = False

    for elf in elf_positions:
        if all([(elf[0] + d[0], elf[1] + d[1]) not in elf_positions for d in directions]):
            elves_sticking_around.add(elf)
        else:
            moved = True
            found_proposal = False
            for i in range(4):
                to_check, move_to = decisions[(i + decision_index) % 4]

                if all([(elf[0] + p[0], elf[1] + p[1]) not in elf_positions for p in to_check]):
                    proposed_move = (elf[0] + move_to[0], elf[1] + move_to[1])
                    found_proposal = True 
                    if proposed_move in proposed_moves:
                        invalid_moves.add(proposed_move)
                        elves_sticking_around.add(proposed_moves[proposed_move])
                        elves_sticking_around.add(elf)
                    else:
                        proposed_moves[proposed_move] = elf
                    break

            if not found_proposal:
                # homie couldn't move
                elves_sticking_around.add(elf)

    elf_positions = (proposed_moves.keys() ^ invalid_moves) | elves_sticking_around

    decision_index += 1

    if not moved:
        break

print(c)