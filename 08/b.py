with open('input', 'r') as f:
    grid = [[int(c) for c in l.strip()] for l in f.readlines()]

    h, w = len(grid), len(grid[0])

    scenic_value = [[0 for j in range(w)] for i in range(h)]

    for i in range(h):
        for j in range(w):
            r_view = 0
            l_view = 0
            d_view = 0
            u_view = 0

            # -> 
            for k in range(j + 1, w):
                r_view += 1
                if grid[i][k] >= grid[i][j]:
                    break
                
            # <- 
            for k in range(j - 1, -1, -1):
                l_view += 1
                if grid[i][k] >= grid[i][j]:
                    break
                

            # v
            for k in range(i + 1, h):
                d_view += 1
                if grid[k][j] >= grid[i][j]:
                    break
                 

            # ^ 
            for k in range(i - 1, -1, -1):
                u_view += 1
                if grid[k][j] >= grid[i][j]:
                    break
            scenic_value[i][j] = r_view * l_view * d_view * u_view

    print(max([item for sublist in scenic_value for item in sublist]))
