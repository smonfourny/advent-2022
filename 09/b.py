directions = {
    "D": (-1, 0),
    "U": (1, 0),
    "R": (0, 1),
    "L": (0, -1)
}

touching = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

visited = set()

knots = [[0, 0] for i in range(10)]

visited.add((0,0))

with open('input', 'r') as f:
    moves = [l.strip().split(' ') for l in f.readlines()]

    for move in moves:
        d = directions[move[0]]
        
        for i in range(int(move[1])):
            # Move head 
            knots[0] = [knots[0][0] + d[0], knots[0][1] + d[1]] 

            for i in range(1, 10):
                head = knots[i-1]

                # Movement vector
                v = [head[0] - knots[i][0], head[1] - knots[i][1]]
                
                if abs(v[0]) + abs(v[1]) < 2:
                    v = [0, 0]
                elif head in [[knots[i][0] + d[0], knots[i][1] + d[1]] for d in touching]:
                    v = [0, 0]
                else:
                    # Move tail
                    if v[0] > 1:
                        v[0] = 1
                    if v[0] < -1:
                        v[0] = -1
                    if v[1] > 1:
                        v[1] = 1
                    if v[1] < -1:
                        v[1] = -1

                knots[i] = [knots[i][0] + v[0], knots[i][1] + v[1]]
            
            # Mark visited
            visited.add(tuple(knots[9]))


print(len(visited))