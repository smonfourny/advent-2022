def get_next_op(pc, ops):
    # get next op
    op = ops[pc]
    if op.startswith('addx'):
        opcode, a = op.split(' ')
        to_add = int(a)
        cycle_length = 2
        execution_state = [cycle_length, to_add]
    else:
        execution_state = [1, 0]

    return execution_state

def draw(crt, cycle):
    row = cycle // 40
    col = (cycle - 1) % 40
    if col in (rx - 1, rx, rx + 1):
        crt[row][col] = '#'

with open('input', 'r') as f:
    ops = [l.strip() for l in f.readlines()]

    rx = 1

    cycle = 1

    crt = [['.' for i in range(40)] for j in range(6)]

    # (remaining cycles, to_add)
    pc = 0
    execution_state = get_next_op(pc, ops)
    signals = []

    while cycle < 240:
        remaining_cycles, to_add = execution_state
        if remaining_cycles == 0:
            rx += to_add
            pc += 1

            if pc >= len(ops):
                break

            execution_state = get_next_op(pc, ops)

        draw(crt, cycle)

        cycle += 1
        execution_state[0] -= 1

    while cycle < 240:
        draw(crt, cycle)

        cycle += 1

    for i in range(len(crt)):
        for j in range(len(crt[0])):
            print(crt[i][j], end='')
        print()