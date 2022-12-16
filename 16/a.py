import re
from collections import deque, defaultdict

class Node:
	def __init__(self, identifier, flow, neighbours):
		self.identifier = identifier
		self.flow = flow
		self.neighbours = neighbours

nodes_by_identifier = {}
non_zero_valves = []

MAX_DEPTH = 30

with open('input', 'r') as f:
	lines = [line.strip() for line in f.readlines()]

	exp = re.compile(r'Valve ([A-Z][A-Z]) has flow rate=(\d+); tunnel[s]* lead[s]* to valve[s]* ([A-Z][A-Z](?:, [A-Z][A-Z])*)')

	for line in lines:
		res = exp.match(line)

		identifier = res.group(1)
		flow = int(res.group(2))
		neighbours = res.group(3).split(', ')

		if flow > 0:
			non_zero_valves.append(identifier)

		# Represents passing through the node without opening the valve
		node = Node(identifier, flow, neighbours)

		nodes_by_identifier[node.identifier] = node

print(non_zero_valves)

shortest_path_to_target_by_origin = {}

def shortest_path_to_target(origin, target):
	q = deque([(origin, 0)])
	visited = set()

	while q:
		node, depth = q.popleft()

		if node in visited:
			continue

		visited.add(node)

		if node == target:
			return depth

		neighbours = nodes_by_identifier[node].neighbours
		for neighbour in neighbours:
			if neighbour in visited:
				continue
			q.append((neighbour, depth + 1))


for target in non_zero_valves + ['AA']:
	for origin in non_zero_valves + ['AA']:
		if target == 'AA' or origin == target:
			continue

		shortest_path_to_target_by_origin[origin+'-'+target] = shortest_path_to_target(origin, target)

paths_to_costs = defaultdict(int)

paths_to_costs[tuple(['AA'])] = 0

def compute_value(curr_node, cost_so_far, path, valid_nodes):
	res = []

	for target in valid_nodes:
		shortest = shortest_path_to_target_by_origin[f'{curr_node}-{target}']

		if shortest + cost_so_far + 1 > MAX_DEPTH:
			continue

		# +1 because we have to open the valve
		total_cost = cost_so_far + shortest_path_to_target_by_origin[f'{curr_node}-{target}'] + 1

		new_path = path + [target]
		node = nodes_by_identifier[target]

		paths_to_costs[tuple(new_path)] = paths_to_costs[tuple(path)] + node.flow * (MAX_DEPTH - total_cost)

		value = paths_to_costs[tuple(path)] + node.flow * (MAX_DEPTH - total_cost)

		res.append((target, total_cost, new_path, value))

	return res

def valves_to_key(valves):
	return tuple(sorted(list(set(valves))))

q = deque([('AA', 0, ['AA'], 0)])

while q:
	curr_node, cost_so_far, path, value = q.popleft()

	res = compute_value(curr_node, cost_so_far, path[:], set(non_zero_valves).difference(path))

	q.extend(res)

print(max(paths_to_costs.values()))
