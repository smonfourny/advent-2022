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

shape_to_choose = { (key[0], outcomes[key]) : key[1] for key in outcomes }

code_to_outcome = {
    'X': 'LOSS',
    'Y': 'DRAW',
    'Z': 'WIN'
}

f = open('input', 'r')

total_score = 0

for line in f.readlines():
    a, b = line.split(' ')
    b = b.replace('\n', '')

    outcome = code_to_outcome[b]

    shape = shape_to_choose[(a, outcome)]

    total_score += points_per_shape[shape]
    total_score += points_per_outcome[outcome]

print(total_score)  