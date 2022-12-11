import re
from collections import deque

with open('input', 'r') as f:
    lines = [l.strip() for l in f.readlines()]
    monkey_count = (len(lines) // 7) + 1

    monkey_items = { k:[] for k in range(monkey_count) }
    monkey_examination = { k:None for k in range(monkey_count) }
    monkey_constant = {k:None for k in range(monkey_count) }
    monkey_test = { k:None for k in range(monkey_count) }
    monkey_next = { k:{} for k in range(monkey_count) }
    monkey_examination_count = { k: 0 for k in range(monkey_count) }

    monkeys = [' '.join(lines[(7 * i):(7 * i)+7]) for i in range(monkey_count)]

    exp = re.compile(r"Monkey \d: Starting items: (\d+(?:, \d+)*) Operation: new = old ([\* | \+]) (\d+|old) Test: divisible by (\d+) If true: throw to monkey (\d) If false: throw to monkey (\d)")

    for i, monkey in enumerate(monkeys):
        r = exp.match(monkey)
        groups = r.groups()

        monkey_items[i] = deque([int(a) for a in groups[0].split(', ')])

        monkey_constant[i] = groups[2]

        if groups[1] == '*':
            monkey_examination[i] = lambda old, cons: old * old if cons == 'old' else old * int(cons)
        elif groups[1] == '+':
            monkey_examination[i] = lambda old, cons: old + old if cons == 'old' else old + int(cons)

        monkey_test[i] = int(groups[3])
        monkey_next[i] = { True: int(groups[4]), False: int(groups[5]) }


    for r in range(20):
        for monkey in range(monkey_count):
            for i in range(len(monkey_items[monkey])):
                item = monkey_items[monkey].popleft()

                # inspect item
                item = monkey_examination[monkey](item, monkey_constant[monkey])
                monkey_examination_count[monkey] += 1

                # decrease worry
                item = item // 3

                # test
                result = item % monkey_test[monkey] == 0

                # next monkey 
                n = monkey_next[monkey][result]

                monkey_items[n].append(item)

    s = sorted([monkey_examination_count[k] for k in monkey_examination_count])
    print(s)
    print(s[-1] * s[-2])
