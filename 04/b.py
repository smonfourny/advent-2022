f = open('input', 'r')

pairs = 0

for l in [l.strip() for l in f.readlines()]:
    a, b = l.split(',')
    a_lower_s, a_upper_s = a.split('-')
    b_lower_s, b_upper_s = b.split('-')

    a_lower, a_upper, b_lower, b_upper = int(a_lower_s), int(a_upper_s), int(b_lower_s), int(b_upper_s), 

    if (a_lower <= b_upper and a_lower >= b_lower) or (b_lower <= a_upper and b_lower >= a_lower):
        pairs += 1 

print(pairs)