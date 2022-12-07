import re

with open('input') as f:
    lines = f.read().splitlines()

    index_of_break = 0

    while lines[index_of_break]:
        index_of_break += 1

    col_length = re.sub(' +', ' ', lines[index_of_break-1].strip()).split(' ')[-1]

    stacks = [[] for i in range(int(col_length))]

    for i in range(index_of_break-2, -1, -1):
        boxes = [lines[i][j:j+3] for j in range(0, 9 * 4, 4)]

        for i, box in enumerate(boxes):
            if box == '   ':
                continue
            stacks[i].append(box)

    # result = re.match('move (\d+) from (\d+) to (\d+)', 'move 2 from 7 to 2')

    for i in range(index_of_break + 1, len(lines)):
        result = re.match('move (\d+) from (\d+) to (\d+)', lines[i])

        boxes_to_move, origin, target = [int(r) for r in result.groups()]

        stacks[target-1].extend(stacks[origin-1][-boxes_to_move:])
        stacks[origin-1] = stacks[origin-1][:-boxes_to_move]

    print([s[-1] for s in stacks])
