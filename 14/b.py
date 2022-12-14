def draw_line(line, grid):
    points = [[int(num) for num in e.split(',')] for e in line.split('->')]

    for i in range(1, len(points)):
        a = points[i - 1]
        b = points[i]

        if a[0] == b[0]:
            if a[1] > b[1]:
                a, b = b, a

            # vertical line
            for k in range(a[1], b[1] + 1):
                grid.add((a[0], k))

        else:
            if a[0] > b[0]:
                a, b = b, a

            # horizontal line
            for k in range(a[0], b[0] + 1):
                grid.add((k, a[1]))

grid = set()

with open('input', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

    for line in lines:
        draw_line(line, grid)

    print(grid)

floor = max([cell[1] for cell in grid]) + 2

print('floor', floor)

r = 0

while True:
    sand_pos = [500, 0]
    moved = True

    while moved:
        if sand_pos[1] == floor - 1:
            break

        if (sand_pos[0], sand_pos[1] + 1) not in grid:
            moved = True
            sand_pos[1] += 1
        elif (sand_pos[0] - 1, sand_pos[1] + 1) not in grid:
            moved = True
            sand_pos[0] -= 1
            sand_pos[1] += 1
        elif (sand_pos[0] + 1, sand_pos[1] + 1) not in grid:
            moved = True
            sand_pos[0] += 1
            sand_pos[1] += 1
        else:
            moved = False

    r += 1

    if (sand_pos[0] == 500 and sand_pos[1] == 0):
        print('top is blocked')
        break
    else:
        grid.add((sand_pos[0], sand_pos[1]))

print(r)