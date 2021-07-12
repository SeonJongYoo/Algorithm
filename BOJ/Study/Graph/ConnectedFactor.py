# 연결요소의 개수

import sys
sys.setrecursionlimit(10000)


def DFS(L, s):
    if L == n:
        return
    else:
        for i in range(1, n+1):
            if graph[s][i] == 1 and visit[i] == 0:
                visit[i] = 1
                res.append(i)
                DFS(L+1, i)


n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u][v] = 1
    graph[v][u] = 1
visit = [0]*(n+1)
cnt = 0
for k in range(1, n+1):
    if visit[k] == 0:
        res = [k]
        visit[k] = 1
        DFS(0, k)
        cnt += 1
print(cnt)