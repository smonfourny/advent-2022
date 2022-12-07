from collections import defaultdict

class Node:
    def __init__(self, identifier, parent):
        self.identifier = identifier
        self.parent = parent

val = defaultdict(int)
root = Node('/', None)

with open('input', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

    # skip first line; we know it's the root
    i = 1

    curr_dir = root

    while i < len(lines):
        # navigation case
        if lines[i].startswith('$ cd'):
            if lines[i] == '$ cd ..':
                curr_dir = curr_dir.parent
            else:
                split_line = lines[i].split(' ')
                curr_dir = Node(curr_dir.identifier + split_line[-1] + '/', curr_dir)

            i += 1

        # file count case
        else:
            i += 1
            while i < len(lines) and lines[i][0] != '$':
                split_line = lines[i].split(' ')
                if split_line[0] != 'dir':
                    added = int(split_line[0])
                    val[curr_dir.identifier] += added

                    p = curr_dir.parent

                    while p:
                        val[p.identifier] += int(split_line[0])
                        p = p.parent

                i += 1

less_than_100000 = [val[k] for k in val if val[k] <= 100000]

print(sum(less_than_100000))