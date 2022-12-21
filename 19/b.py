import re
from collections import defaultdict, deque
import copy
from math import ceil

class Blueprint:
    def __init__(self, robot_id, costs):
        self.id = robot_id
        self.costs = costs

bps = []

with open('input', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

    for l in lines:
        exp = re.compile(r'Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.')
        res = exp.match(l)

        robot_id = int(res.group(1))
        ore_cost = defaultdict(int)
        clay_cost = defaultdict(int)
        obsidian_cost = defaultdict(int)
        geode_cost = defaultdict(int)

        costs = defaultdict(dict)

        costs["ore"]["ore"] = int(res.group(2))
        costs["clay"]["ore"] = int(res.group(3)) 
        costs["obsidian"]["ore"] = int(res.group(4))
        costs["obsidian"]["clay"] = int(res.group(5))
        costs["geode"]["ore"] = int(res.group(6))
        costs["geode"]["obsidian"] = int(res.group(7))

        robot = Blueprint(robot_id, costs)

        bps.append(robot)

max_geode_by_id = defaultdict(int)
resource_tags = ['ore', 'clay', 'obsidian', 'geode']

def possible_paths(bp, g, t, maxes):
    paths = []

    for resource in resource_tags:
        if resource == 'geode' and not g['obsidian_robot']:
            # can't build yet
            continue

        if resource == 'obsidian' and not g['clay_robot']:
            # can't build yet
            continue

        if resource == 'geode' or g[resource + '_robot'] < maxes[resource]:
            time_to_robot = max([max(bp.costs[resource][k] - g[k] + g[k+'_robot'] - 1, 0) // g[k + '_robot'] for k in bp.costs[resource]]) + 1
            if t - time_to_robot >= 0:
                paths.append([time_to_robot, resource])

    return paths

def hashed_game_state(t, g):
    return (t, g['ore'], g['clay'], g['obsidian'], g['geode'], g['ore_robot'], g['clay_robot'], g['obsidian_robot'], g['geode_robot'])

def max_if_do_nothing(t, g):
    return g['geode'] + t * g['geode_robot']

def theoretical_max(t, g):
    # max if do nothing + building a geode cracker every remaining turn
    return max_if_do_nothing(t, g) + (t - 1) * t // 2

def traverse(bp):
    # count of each resource (ore, clay, obsidian, geode, ore_robot, clay_robot, obsidian_robot, geode_robot)
    game_state = defaultdict(int)
    game_state['ore_robot'] = 1

    maxes = { k: max([ bp.costs[robot].get(k,0) for robot in bp.costs ]) for k in ['ore', 'clay', 'obsidian'] }

    visited = set()

    q = deque([(32, game_state)])

    while q:
        print(len(q), f'max so far {max_geode_by_id[bp.id]}')
        t, g = q.popleft()

        if theoretical_max(t, g) < max_geode_by_id[bp.id]:
            continue

        valid_paths = possible_paths(bp, g, t, maxes) 

        if not valid_paths:
            # max with what we have 
            max_geode_by_id[bp.id] = max(max_geode_by_id[bp.id], max_if_do_nothing(t, g))
            continue

        for p in valid_paths:
            time_taken, robot = p[0], p[1]

            # print(p)
            new_g = copy.deepcopy(g)

            new_t = t - p[0]

            new_g['ore'] += new_g.get('ore_robot', 0) * time_taken
            new_g['clay'] += new_g.get('clay_robot', 0) * time_taken
            new_g['obsidian'] += new_g.get('obsidian_robot', 0) * time_taken
            new_g['geode'] += new_g.get('geode_robot', 0) * time_taken

            for k in bp.costs[robot]:
                # print(f'removing {bp.costs[robot][k]} {k} to build {robot} robot')
                new_g[k] -= bp.costs[robot][k]
            new_g[robot+'_robot'] += 1

            max_geode_by_id[bp.id] = max(max_geode_by_id[bp.id], new_g['geode'])

            if hashed_game_state(new_t, new_g) not in visited:
                visited.add(hashed_game_state(new_t, new_g))
                q.append((new_t, new_g))

for bp in bps:
    if bp.id > 3:
        continue

    traverse(bp)

print(max_geode_by_id)

res = 1

for k in max_geode_by_id:
    res *= max_geode_by_id[k]

print(res)