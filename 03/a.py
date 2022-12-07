f = open('input', 'r')

packs = [l.strip() for l in f.readlines()]

sum_of_priorities = 0

for p in packs:
    s = set()
    i = 0
    l = len(p)
    while i < l // 2:
        s.add(p[i])
        i += 1 

    while i < l:
        if p[i] in s:
            sum_of_priorities += ord(p[i]) - 96 if p[i].islower() else ord(p[i]) - 38
            break
        i += 1

print(sum_of_priorities)