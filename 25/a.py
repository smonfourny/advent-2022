from collections import deque

with open('input', 'r') as f:
    nums = [l.strip() for l in f.readlines()]

m = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2
}

m_rev = {
    2: '2',
    1: '1',
    0: '0',
    -1: '-',
    -2: '='
}

s = 0

for n in nums:
    ss = 0
    for i, c in enumerate(reversed(n)):
        ss += m[c] * pow(5, i)

    print(ss)
    s += ss

print('total', s)

c = s
res = ''
held = False

while c:
    rem = c % 5 
    if held:
        rem += 1
    if rem > 2:
        k = rem - 5
        res += m_rev[k]
        held = True
    else:
        held = False
        res += m_rev[rem]
    c = c // 5

print(res[::-1])
