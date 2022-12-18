points = []

directions = [
    [1, 0, 0],
    [-1, 0, 0],
    [0, 1, 0],
    [0, -1, 0],
    [0, 0, 1],
    [0, 0, -1]
]

with open('input', 'r') as f:
    lines = [l.strip() for l in f.readlines()]
    for l in lines:
        vals = [int(val) for val in l.split(',')]
        points.append(vals)

s = set([tuple(p) for p in points])

total_exposed = 0

for p in points:
    exposed_sides = 6 
    for d in directions:
        if (p[0] + d[0], p[1] + d[1], p[2] + d[2]) in s:
            exposed_sides -= 1

    total_exposed += exposed_sides

print(total_exposed)