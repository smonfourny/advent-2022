import re

class OpNode:
    def __init__(self, node_id, l, op, r):
        self.id = node_id
        self.op = op
        self.l = l
        self.r = r

class ValNode:
    def __init__(self, node_id, val):
        self.id = node_id
        self.val = val

nodes_by_key = {}

digit_exp = re.compile(r'([a-z]+): (-?\d+)')
op_exp = re.compile(r'([a-z]+): ([a-z]+) ([+\-/*]) ([a-z]+)')

with open('input', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

    for line in lines:
        digit_res = digit_exp.match(line)
        if digit_res:
            nodes_by_key[digit_res.group(1)] = ValNode(digit_res.group(1), digit_res.group(2))
        else:
            op_res = op_exp.match(line)
            nodes_by_key[op_res.group(1)] = OpNode(op_res.group(1), op_res.group(2), op_res.group(3), op_res.group(4))

def traverse(node_key):
    node = nodes_by_key[node_key]

    if isinstance(node, ValNode):
        return node.val

    l = traverse(node.l)
    r = traverse(node.r)

    return eval(str(l) + node.op + str(r))

print(traverse('root'))