f = open('./input', 'r')

curr = 0
max_so_far = 0

for l in f.readlines():
    striped_line = l.strip('\n')
    if not striped_line:
        max_so_far = max(curr, max_so_far)
        curr = 0
        continue

    curr += int(striped_line)

print(max(max_so_far, curr))