from collections import deque
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    Q = deque(map(int, input().split()))
    ch = deque()
    for i in range(len(Q)):
        ch.append(0)
    ch[m] = 1
    res = Q[m]
    cnt = 0
    if len(Q) == 1:
        print(1)
        continue
    while Q:
        Max = max(Q)
        x = Q.popleft()
        y = ch.popleft()
        if x < Max:
            Q.append(x)
            ch.append(y)
            continue
        cnt += 1
        if x == res and y == 1:
            print(cnt)
            break
