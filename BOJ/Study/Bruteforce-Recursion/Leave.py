# 퇴사

import sys


def DFS(L, cost):
    global Max
    if L == n+1:
        Max = max(cost, Max)
    else:
        if L + cons[L][0] < n+2:
            DFS(L+cons[L][0], cost + cons[L][1])
        DFS(L+1, cost)


n = int(sys.stdin.readline().rstrip())
cons = [(0, 0)]
for _ in range(n):
    t, p = map(int, sys.stdin.readline().rstrip().split())
    cons.append((t, p))
Max = 0
DFS(1, 0)
print(Max)
