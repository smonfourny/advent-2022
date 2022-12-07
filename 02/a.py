points_per_shape = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

points_per_outcome = {
    'LOSS': 0,
    'DRAW': 3,
    'WIN': 6
}

outcomes = {
    ('A', 'X'): 'DRAW',
    ('A', 'Y'): 'WIN',
    ('A', 'Z'): 'LOSS',
    ('B', 'X'): 'LOSS',
    ('B', 'Y'): 'DRAW',
    ('B', 'Z'): 'WIN',
    ('C', 'X'): 'WIN',
    ('C', 'Y'): 'LOSS',
    ('C', 'Z'): 'DRAW',
}

f = open('input', 'r')

total_score = 0

for line in f.readlines():
    a, b = line.split(' ')
    b = b.replace('\n', '')
    outcome_points = points_per_outcome[outcomes[(a, b)]]
    shape_points = points_per_shape[b]
    total_score += outcome_points + shape_points

print(total_score)  