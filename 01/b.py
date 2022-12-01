import heapq

f = open('./input', 'r')

h = []

curr = 0

for l in f.readlines():
    striped_line = l.strip('\n')
    if not striped_line:
        heapq.heappush(h, -curr)
        curr = 0
        continue

    curr += int(striped_line)

print(sum([-heapq.heappop(h) for i in range(3)]))