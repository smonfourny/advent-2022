from collections import defaultdict
import re
import heapq

g = defaultdict(lambda: defaultdict(dict))

sensor_beacon_pairs = []

SEARCH_SPACE_SIZE = 4000000

def compute_overlaps(position, manhattan_per_sensor):
    # print(position)
    count = 0
    for sensor in manhattan_per_sensor:
        # print('sensor', sensor)
        manhattan_to_pos =  abs(sensor[0] - position[0]) + abs(sensor[1] - position[1])
        if manhattan_to_pos <= manhattan_per_sensor[sensor]:
            count += 1 

    return count

with open('input', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

    exp = re.compile(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")

    for line in lines:
        res = exp.match(line)

        sensor_beacon_pairs.append([(int(res.group(1)), int(res.group(2))), (int(res.group(3)), int(res.group(4)))])

manhattan_per_sensor = { pair[0]: abs(pair[0][0] - pair[1][0]) + abs(pair[0][1] - pair[1][1]) for pair in sensor_beacon_pairs }

for sensor in manhattan_per_sensor:
    print(sensor)
    d = manhattan_per_sensor[sensor]
    for i in range(0, d+1):
        right, left = sensor[1] + (d - i) + 1, sensor[1] - (d - i) + 1
        row = sensor[0] + i

        if row < 0 or row > SEARCH_SPACE_SIZE:
            continue

        if sensor == (8,7):
            print('row', row)
            print('left, right', left, right)

        if left >= 0 and left < SEARCH_SPACE_SIZE + 1:
            if compute_overlaps((row, left), manhattan_per_sensor) == 0:
                print('found:', (row, left))
                exit(0)
        if right >= 0 and right < SEARCH_SPACE_SIZE + 1:
            if compute_overlaps((row, right), manhattan_per_sensor) == 0:
                print('found:', (row, right))
                exit(0)
    if (sensor[0] + d + 1) >= 0 and sensor[0] + d + 1 < SEARCH_SPACE_SIZE + 1:
        if compute_overlaps((sensor[0] + d + 1, sensor[1]), manhattan_per_sensor) == 0:
            print('found:', (sensor[0] + d + 1, sensor[1]))
            exit(0)
    if (sensor[0] - d - 1) >= 0 and sensor[0] - d - 1 < SEARCH_SPACE_SIZE + 1:
        if compute_overlaps((sensor[0] - d - 1, sensor[1]), manhattan_per_sensor) == 0:
            print('found:', (sensor[0] - d - 1, sensor[1]))
            exit(0)

