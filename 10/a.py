with open('input', 'r') as f:
    ops = [l.strip() for l in f.readlines()]

    rx = 1

    cycle = 1

    signals = []
    for op in ops:
        if len(signals) == 6:
            break



        if op.startswith('addx'):
            opcode, a = op.split(' ')
            to_add = int(a)
            cycle_length = 2
        else:
            to_add = 0
            cycle_length = 1

        for i in range(cycle_length):
            if (cycle) % 40 == 20:
                signals.append(cycle * rx)
            cycle += 1

        rx += to_add

    while cycle < 220:
        if (cycle) % 40 == 20:
            signals.append(cycle * rx)
        cycle += 1

    print(sum(signals))