import re
from collections import deque

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

paths_to_costs = {}

paths_to_costs[tuple(['AA'])] = 0

q = deque([('AA', 0, ['AA'])])

while q:
	print(len(paths_to_costs))
	curr_node, cost_so_far, path = q.popleft()

	for target in non_zero_valves:
		if target in path:
			continue

		sq = deque([(curr_node, 0)])

		visited = set()

		while sq:
			visiting, depth = sq.popleft()

			if visiting in visited:
				continue

			visited.add(visiting)

			if depth + cost_so_far > MAX_DEPTH:
				continue

			if visiting == target:
				# +1 because we have to open the valve
				total_cost = cost_so_far + depth + 1

				new_path = path + [target]
				node = nodes_by_identifier[target]

				paths_to_costs[tuple(new_path)] = paths_to_costs[tuple(path)] + node.flow * (MAX_DEPTH - total_cost)

				q.append((target, total_cost, new_path))
				continue

			node = nodes_by_identifier[visiting]

			for neighbour in node.neighbours:
				if neighbour in visited:
					continue

				sq.append((neighbour, depth + 1))

print(max(paths_to_costs.values()))
