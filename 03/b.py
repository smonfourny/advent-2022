import itertools
from collections import defaultdict

f = open('input', 'r')

packs = [l.strip() for l in f.readlines()]

sum_of_priorities = 0

# there's surely a cleaner way to do this but i'm lazy
three_packs = [[i[1] for i in list(v)] for k, v in itertools.groupby(enumerate(packs), lambda k: k[0] // 3)]

for t in three_packs:
    s = defaultdict(int)

    for p in t:
        k = set()
        for c in p:
            if c not in k:
                s[c] += 1
                if s[c] == 3:
                    sum_of_priorities += ord(c) - 96 if c.islower() else ord(c) - 38
            k.add(c)

print(sum_of_priorities)