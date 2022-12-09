# # this is only for the example
# def print_map(head, tail):
#     print()
#     for i in reversed(range(5)):
#         for j in range(6):
#             if [i, j] == head:
#                 print('H', end = '')
#             elif [i, j] == tail:
#                 print('T', end = '')
#             else:
#                 print('.', end = '')
#         print()
#     print()

directions = {
    "D": (-1, 0),
    "U": (1, 0),
    "R": (0, 1),
    "L": (0, -1)
}

touching = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

visited = set()

head = [0, 0]
tail = [0, 0]

visited.add(tuple(tail))

# print_map(head, tail)

with open('input', 'r') as f:
    moves = [l.strip().split(' ') for l in f.readlines()]

    for move in moves:
        d = directions[move[0]]
        
        for i in range(int(move[1])):
            # Move head 
            head = [head[0] + d[0], head[1] + d[1]] 

            # Movement vector
            v = [head[0] - tail[0], head[1] - tail[1]]

            if abs(v[0]) + abs(v[1]) < 2:
                v = [0, 0]
            elif head in [[tail[0] + d[0], tail[1] + d[1]] for d in touching]:
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

            tail = [tail[0] + v[0], tail[1] + v[1]]

            # print_map(head, tail)
            
            # Mark visited
            visited.add(tuple(tail))

print(len(visited))

