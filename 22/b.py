import re

file_map_path = 'input_map'
file_path = 'input'
pos = (0, 50)

with open(file_map_path, 'r') as fm:
    lines = [l.rstrip() for l in fm.readlines()]

    height = len(lines)
    width = max([len(l) for l in lines])

    grid = [[l[i] if i < len(l) else ' ' for i in range(width)] for l in lines]

with open(file_path, 'r') as f:
    exp = re.compile(r'([A-Z]|\d+)')
    r = exp.finditer(f.read())

    moves = [m.group(0) for m in r]

top_left_by_face = {
    1: (0, 50),
    2: (0, 100),
    3: (50, 50),
    4: (100, 0),
    5: (100, 50),
    6: (150, 0)
}

def cube_face(r, c):
    if 0 <= r < 50 and 50 <= c < 100:
        return 1
    if 0 <= r < 50 and 100 <= c < 150:
        return 2
    if 50 <= r < 100 and 50 <= c < 100:
        return 3
    if 100 <= r < 150 and 0 <= c < 50:
        return 4
    if 100 <= r < 150 and 50 <= c < 100:
        return 5
    if 150 <= r < 200 and 0 <= c < 50:
        return 6

    return None

# compute new pos based on original pos and which face you teleported to
def teleport(offset, new_face, new_orientation):
    top_left = top_left_by_face[new_face]

    res = [0, 0]

    if new_orientation == (0, 1):
        return (top_left[0] + offset, top_left[1])
    elif new_orientation == (0, -1):
        return (top_left[0] + offset, top_left[1] + 49)
    elif new_orientation == (1, 0):
        return (top_left[0], top_left[1] + offset)
    else:
        return (top_left[0] + 49, top_left[1] + offset)

    return res

def get_offset(pos, face, orientation, is_inverted):
    top_left = top_left_by_face[face]
    offset_part = orientation.index(0)

    off = pos[offset_part] - top_left[offset_part]

    return 49 - off if is_inverted else off

vals = {
    (0, 1): 0,
    (1, 0): 1,
    (0, -1): 2,
    (-1, 0): 3
}

# side and edge met to new face and orientation... only 14 mappings to define, not the end of the world (she said through tears)
face_or_to_new_face_new_or = {
    1: {
        # L
        (0, -1): (4, (0, 1), True), # 4 R inverted
        # U
        (-1, 0): (6, (0, 1), False) # 6 R normal
    },
    2: {
        # R
        (0, 1): (5, (0, -1), True), # 5 L
        # D
        (1, 0): (3, (0, -1), False), # 3 L
        # U
        (-1, 0): (6, (-1, 0), False) # 6 U
    },
    3: {
        # R
        (0, 1): (2, (-1, 0), False), # 2 U
        # L
        (0, -1): (4, (1, 0), False) # 4 D
    },
    4: {
        # L
        (0, -1): (1, (0, 1), True), # 1 R 
        # U
        (-1, 0): (3, (0, 1), False) 
    },
    5: {
        # R
        (0, 1): (2, (0, -1), True), # 2 L
        # D
        (1, 0): (6, (0, -1), False) # 6 L
    },
    6: {
        # R
        (0, 1): (5, (-1, 0), False), # 5 U
        # D
        (1, 0): (2, (1, 0), False), # 2 D
        # L
        (0, -1): (1, (1, 0), False) # 1 D
    }
}

# i increasing = R turn, i decreasing = L turn
# R, D, L, U
orientations = [(0, 1), (1, 0), (0, -1), (-1, 0)]
o = 0

for move in moves:
    if move.isnumeric():
        for i in range(int(move)):
            # take a step
            np = (pos[0] + orientations[o][0], pos[1] + orientations[o][1])

            new_face = cube_face(np[0], np[1])

            if not new_face:
            # if np[0] >= height or np[1] >= width or np[0] < 0 or np[1] < 0 or grid[np[0]][np[1]] == ' ':
                # find new face and orientation
                f = cube_face(pos[0], pos[1])
                new_f, new_o, is_inverted = face_or_to_new_face_new_or[f][orientations[o]]

                # what's the new position?
                offset = get_offset(pos, f, orientations[o], is_inverted)

                temp = teleport(offset, new_f, new_o)

                # if there is a wall there, do nothing 
                if grid[temp[0]][temp[1]] == '#':
                    break

                # else teleport
                o = orientations.index(new_o)
                np = temp

            # if wall -> stop moving
            elif grid[np[0]][np[1]] == '#':
                break

            pos = np
    else:
        if move == 'R':
            o = (o + 1) % len(orientations)
        else:
            o = (o - 1) % len(orientations)

res = 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + vals[orientations[o]]

print(res)