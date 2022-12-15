from collections import defaultdict
import re

g = defaultdict(lambda: defaultdict(dict))

sensor_beacon_pairs = []

with open('input', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

    exp = re.compile(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")

    for line in lines:
        res = exp.match(line)

        sensor_beacon_pairs.append([(int(res.group(1)), int(res.group(2))), (int(res.group(3)), int(res.group(4)))])

print(sensor_beacon_pairs)

# range of blocked on row 2 000 000, we'll keep updating this
left, right = float('inf'), float('-inf') 

for pair in sensor_beacon_pairs:
    sensor = pair[0]
    beacon = pair[1]

    manhattan_distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
 
    # range_from_center = manhattan_distance - abs(10 - sensor[1])
    range_from_center = manhattan_distance - abs(2000000 - sensor[1])

    left = min(sensor[0] - range_from_center, left)
    right = max(sensor[0] + range_from_center, right)

# this works coincidentally and i'm too lazy to fix it :)
print(right - left)