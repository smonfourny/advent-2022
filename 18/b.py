from collections import deque
from functools import lru_cache

points = []

directions = [
    [1, 0, 0],
    [-1, 0, 0],
    [0, 1, 0],
    [0, -1, 0],
    [0, 0, 1],
    [0, 0, -1]
]

max_x = float('-inf')
max_y = float('-inf')
max_z = float('-inf')
min_x = float('inf')
min_y = float('inf')
min_z = float('inf')

with open('input', 'r') as f:
    lines = [l.strip() for l in f.readlines()]
    for l in lines:
        vals = [int(val) for val in l.split(',')]
        max_x, min_x = max(max_x, vals[0]), min(min_x, vals[0])
        max_y, min_y = max(max_y, vals[1]), min(min_y, vals[1])
        max_z, min_z = max(max_z, vals[2]), min(min_z, vals[2])

        points.append(vals)

s = set([tuple(p) for p in points])
air = set()

total_exposed = 0

for p in points:
    exposed_sides = 6 
    for d in directions:
        cube = (p[0] + d[0], p[1] + d[1], p[2] + d[2])

        if cube in s:
            exposed_sides -= 1
        else:
            if cube[0] > min_x and cube[0] < max_x and cube[1] > min_y and cube[1] < max_y and cube[2] > min_z and cube[2] < max_z:
                air.add(cube)

    total_exposed += exposed_sides

visited = set()

exposed_outside = set()

def traversal(b):
    q = deque([(b, [])])
    visited = set()

    while q:
        a, path = q.pop()

        if a in visited:
            continue

        visited.add(a)

        for d in directions:
            cube = (a[0] + d[0], a[1] + d[1], a[2] + d[2])

            if cube in visited:
                continue

            if cube not in s:
                if cube in exposed_outside:
                    exposed_outside.update(path)
                    exposed_outside.add(cube)
                    exposed_outside.add(a)
                    continue

                if cube[0] <= min_x or cube[0] >= max_x or cube[1] <= min_y or cube[1] >= max_y or cube[2] <= min_z or cube[2] >= max_z:
                    exposed_outside.update(path)
                    exposed_outside.add(cube)
                    exposed_outside.add(a)
                    continue

                new_path = path + [a]

                q.append((cube, new_path))
        
for i, a in enumerate(air):
    exp = traversal(a)

unexposed_air = air.difference(exposed_outside)

for a in unexposed_air:
    removed_sides = 0
    for d in directions:
        cube = (a[0] + d[0], a[1] + d[1], a[2] + d[2])

        if cube in s:
            removed_sides += 1

    total_exposed -= removed_sides

print(total_exposed)

