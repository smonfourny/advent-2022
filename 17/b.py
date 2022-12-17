import copy

f = open('test_input', 'r')

sequence = [c for l in f.readlines() for c in l]

print(len(sequence))

f.close()

LOOPS = 1000000000000

shapes = [
    [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 1, 1, 1]
    ],
    [
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0]
    ],
    [
        [0, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 1, 0],
        [1, 1, 1, 0]
    ],
    [
        [1, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 0]
    ],
    [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [1, 1, 0, 0]
    ]
]

def create_game_state(shape_index, sequence_index, grid, top_of_tower):
    # arbitrarily large subset of grid; unlikely we'd run into the exact same 
    # configuration of this size if cycle is not present. 
    sub_grid = grid[top_of_tower:top_of_tower + 40]
    flat_grid = [item for sub in sub_grid for item in sub]

    return (shape_index, sequence_index, tuple(flat_grid))


grid = [[0 for i in range(7)] for j in range(10000)]

grid.append([1 for i in range(7)])

top_of_tower = len(grid) - 1

overall_moves = 0

game_state_to_tower_height = {}

i = 0

actual_top = 0

skipped = False

while i < LOOPS:
    # start 3 squares away from top of tower
    starting_height = top_of_tower - 3

    # start offset by 2
    offset = 2
    
    shape_index = i % len(shapes)

    shape = shapes[shape_index]

    k = 0

    stopped = False

    sequence_index = overall_moves % len(sequence)

    if len(grid) - top_of_tower >= 40 and not skipped:        
        game_state = create_game_state(shape_index, sequence_index, grid, starting_height)
        if game_state in game_state_to_tower_height:
            t, last_i = game_state_to_tower_height[game_state]
            diff_since_last = t - top_of_tower
            cycles = i - last_i

            actual_top += ((LOOPS - i) // cycles) * diff_since_last
            i = LOOPS - (LOOPS - i) % cycles

            print('remaining cycles', cycles)
            print(diff_since_last)
            skipped = True
        else:
            game_state_to_tower_height[game_state] = (top_of_tower, i)

    while starting_height + k < len(grid) and not stopped:
        sequence_index = overall_moves % len(sequence)

        movement = sequence[sequence_index]

        valid = True

        if movement == '<':
            for h, line in enumerate(shape):
                for w, val in enumerate(line):
                    y, x = starting_height + k - 4 + h, offset - 1 + w

                    if x < 0 or x >= len(grid[0]):
                        if val:
                            valid = False
                        continue

                    g = grid[y][x]
                    if g & val:
                        valid = False

            if valid:
                offset -= 1

        if movement == '>':

            for h, line in enumerate(shape):
                for w, val in enumerate(line):
                    y, x = starting_height + k - 4 + h, offset + 1 + w

                    if x < 0 or x >= len(grid[0]):
                        if val:
                            valid = False
                        continue

                    g = grid[y][x]
                    if g & val:
                        valid = False

            if valid:                
                offset += 1

        overall_moves += 1

        went_down = True

        for h, line in enumerate(shape):
            for w, val in enumerate(line):
                if starting_height + k + 1 - 4 + h >= len(grid):
                    went_down = not val
                    continue

                # wouldn't have been positioned like this if not valid
                if offset + w >= 0 and offset + w < len(grid[0]): 
                    g = grid[starting_height + k + 1 - 4 + h][offset + w]
                    if g & val:
                        went_down = False

        if went_down:                
            k += 1
        else:
            stopped = True

    new_starting_height = starting_height

    # update grid with where the thing is 
    for h in range(4):
        for w in range(4):
            y, x = starting_height + k - 4 + h, offset + w

            if y < len(grid) and y >= 0 and x < len(grid[0]) and x >= 0:
                grid[y][x] |= shape[h][w]
                if grid[y][x]:
                    top_of_tower = min(starting_height + k - 4 + h, top_of_tower)

    i += 1

print(len(grid) - top_of_tower - 1 + actual_top)
