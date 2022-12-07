from collections import deque

with open('input', 'r') as f:
    q = deque([])

    i = 0
    for c in f.read():
        i += 1

        q.append(c)

        if len(q) > 14:
            q.popleft()
                
        if len(set(q)) == 14:
            print(q)
            break
    
    print(i)


