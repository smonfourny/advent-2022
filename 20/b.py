from collections import defaultdict
import copy

with open('input', 'r') as f:
    lines = [int(l.strip()) * 811589153 for l in f.readlines()]

d = defaultdict(int)
deduped = []

print([d[0] for d in deduped])

for l in lines:
    deduped.append((l, d[l]))
    d[l] += 1

master = copy.deepcopy(deduped)

for i in range(10):
    for d in master:
        i = deduped.index(d)
        elem = deduped.pop(i)
        if (i + elem[0]) % len(deduped) == 0:
            deduped.append(elem)
        else:
            deduped.insert((i + elem[0]) % len(deduped), elem)

i_0 = deduped.index((0, 0))

print('result')
print(deduped[(i_0 + 1000) % len(deduped)][0] + deduped[(i_0 + 2000) % len(deduped)][0] + deduped[(i_0 + 3000) % len(deduped)][0])

print(f'1000th {deduped[(i_0 + 1000) % len(deduped)]}')
print(f'2000th {deduped[(i_0 + 2000) % len(deduped)]}')
print(f'3000th {deduped[(i_0 + 3000) % len(deduped)]}')