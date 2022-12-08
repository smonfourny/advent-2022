with open('input', 'r') as f:
    grid = [[int(c) for c in l.strip()] for l in f.readlines()]

    h, w = len(grid), len(grid[0])

    l = [[-1 for j in range(w)] for i in range(h)]
    r = [[-1 for j in range(w)] for i in range(h)]
    u = [[-1 for j in range(w)] for i in range(h)]
    d = [[-1 for j in range(w)] for i in range(h)]

    visible_trees = 0

    for i in range(h):
        for j in range(w):
            if i > 0:
                d[i][j] = max(grid[i-1][j], d[i-1][j])

            if j > 0:
                l[i][j] = max(grid[i][j-1], l[i][j-1])

    for i in range(h - 1, -1, -1):
        for j in range(w - 1, -1, -1):
            if i < h - 1:
                u[i][j] = max(grid[i+1][j], u[i+1][j])

            if j < w - 1:
                r[i][j] = max(grid[i][j+1], r[i][j+1])

    for i in range(h):
        for j in range(w):
            t = grid[i][j]

            if t > l[i][j] or t > r[i][j] or t > u[i][j] or t > d[i][j]:
                visible_trees += 1

    print(visible_trees)
