from collections import deque

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

with open('input', 'r') as f:
    grid = [[c for c in line.strip()] for line in f.readlines()]

    # start position hardcoded for simplicity
    # start_position = [[0, 0], 0]
    start_position = [[20, 0], 0]

    queue = deque([start_position])

    visited = set()

    found = False

    while queue and not found:
        position, depth = queue.popleft()

        # don't need to visit again, already have
        if (position[0], position[1]) in visited:
            continue

        visited.add((position[0], position[1]))

        height = ord('a') if grid[position[0]][position[1]] == 'S' else ord(grid[position[0]][position[1]])

        for d in directions:
            new_position = [position[0] + d[0], position[1] + d[1]]
            new_depth = depth + 1

            if (new_position[0], new_position[1]) in visited:
                continue

            if new_position[0] >= len(grid) or new_position[1] >= len(grid[0]) or new_position[0] < 0 or new_position[1] < 0:
                continue

            new_height = ord('z') if grid[new_position[0]][new_position[1]] == 'E' else ord(grid[new_position[0]][new_position[1]])

            if new_height - height <= 1:
                if grid[new_position[0]][new_position[1]] == 'E':
                    print(f'found top after {new_depth} steps at position {new_position}')
                    found = True
                    break
                queue.append([new_position, new_depth])






        