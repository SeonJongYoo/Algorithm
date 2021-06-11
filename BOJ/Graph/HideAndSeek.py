# 숨바꼭질

import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
Q = deque()
Q.append(n)
time = 0
MAX_DIS = 100001
visit = [0]*MAX_DIS
dx = [-1, 1, 0]
flag = False
route = [(0, n, time)]
while Q:
    if flag:
        break
    size = len(Q)
    for _ in range(size):
        tmp = Q.popleft()
        visit[tmp] = 1
        dx[2] = tmp
        if tmp == k:
            flag = True
            print(time)
            curr = tmp
            res = [curr]
            for k in range(len(route)-1, 0, -1):
                if curr == route[k][1] and route[k][2] == time-1:
                    res.append(route[k][0])
                    curr = route[k][0]
                    time -= 1
            for loc in range(len(res)-1, -1, -1):
                print(res[loc], end=" ")
            break
        for i in range(3):
            bx = tmp + dx[i]
            if 0 <= bx < MAX_DIS and visit[bx] == 0:
                Q.append(bx)
                route.append((tmp, bx, time))
    time += 1
