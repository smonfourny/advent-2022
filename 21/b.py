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

class HumanNode:
    def __init__(self, node_id):
        self.id = node_id

nodes_by_key = {}

digit_exp = re.compile(r'([a-z]+): (-?\d+)')
op_exp = re.compile(r'([a-z]+): ([a-z]+) ([+\-/*]) ([a-z]+)')

with open('input', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

    for line in lines:
        digit_res = digit_exp.match(line)
        if digit_res:
            if op_res.group(1) == 'humn':
                nodes_by_key[digit_res.group(1)] = HumanNode(digit_res.group(1))
            else:
                nodes_by_key[digit_res.group(1)] = ValNode(digit_res.group(1), digit_res.group(2))
        else:
            op_res = op_exp.match(line)
            if op_res.group(1) == 'root':
                nodes_by_key[op_res.group(1)] = OpNode(op_res.group(1), op_res.group(2), '=', op_res.group(4))
            else:
                nodes_by_key[op_res.group(1)] = OpNode(op_res.group(1), op_res.group(2), op_res.group(3), op_res.group(4))

def find_humn(node_key):
    node = nodes_by_key[node_key]

    if isinstance(node, ValNode):
        return node_key == 'humn'

    l = find_humn(node.l)
    r = find_humn(node.r)

    return l or r

def eval_node(node_key):
    node = nodes_by_key[node_key]

    if isinstance(node, ValNode):
        return node.val

    l = eval_node(node.l)
    r = eval_node(node.r)

    return eval(str(l) + node.op + str(r))

def match_to_target(node_key, target):
    node = nodes_by_key[node_key]

    if node.id == 'humn':
        return target

    # find which side of the tree humn is on
    humn_is_left = find_humn(node.l)

    if humn_is_left:
        val_to_match = eval_node(node.r)
        if node.op == '=':
            return match_to_target(node.l, target)
        elif node.op == '+':
            new_t = eval(f'{target} - {val_to_match}')
            return match_to_target(node.l, new_t)
        elif node.op == '-':
            # target = l - val_to_match
            # target + val_to_match = l
            new_t = eval(f'{target} + {val_to_match}')
            return match_to_target(node.l, new_t)
        elif node.op == '*':
            new_t = eval(f'{target} / {val_to_match}')
            return match_to_target(node.l, new_t)
        elif node.op == '/':
            new_t = eval(f'{target} * {val_to_match}')
            return match_to_target(node.l, new_t)
    else:
        val_to_match = eval_node(node.l)
        if node.op == '=':
            return match_to_target(node.r, target)
        elif node.op == '+':
            new_t = eval(f'{target} - {val_to_match}')
            return match_to_target(node.r, new_t)
        elif node.op == '-':
            # target = val_to_match - l
            # l = val_to_match - target
            new_t = eval(f'{val_to_match} - {target}')
            return match_to_target(node.r, new_t)
        elif node.op == '*':
            new_t = eval(f'{target} / {val_to_match}')
            return match_to_target(node.r, new_t)
        elif node.op == '/':
            # target = val_to_match / l
            # target * l = val_to_match
            # l = val_to_match / target
            new_t = eval(f'{val_to_match} / {target}')
            return match_to_target(node.r, new_t)

node = nodes_by_key['root']

# find which side of the tree humn is on
humn_is_left = find_humn(node.l)

if humn_is_left:
    res = match_to_target(node.l, eval_node(node.r))
else:
    res = match_to_target(node.r, eval_node(node.l))
print(res)








