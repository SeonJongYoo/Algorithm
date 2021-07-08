# 차이를 최대로

import sys


def DFS(L):
    global Max
    if L == n:
        ans = 0
        for i in range(0, n-1):
            ans += abs(res[i] - res[i+1])
        Max = max(ans, Max)
    else:
        for i in range(1, n+1):
            if visit[i] == 0:
                visit[i] = 1
                res.append(inp[i])
                DFS(L+1)
                res.pop()
                visit[i] = 0


n = int(sys.stdin.readline().rstrip())
inp = list(map(int, sys.stdin.readline().rstrip().split()))
inp.insert(0, 0)
res = []
visit = [0]*(n+1)
Max = -1000
DFS(0)
print(Max)