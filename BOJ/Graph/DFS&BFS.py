# DFS와 BFS
from collections import deque


# DFS
def DFS(L1, vt):
    if L1 == n:
        return
    for i in range(1, n + 1):
        if i == vt:
            continue
        if graph[vt][i] == 1 and ch1[i] == 0:
            ch1[i] = 1
            dfs.append(i)
            DFS(L1+1, i)


n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
ch1 = [0] * (n + 1)
dfs = []
edge1 = 0
flag1 = False
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
ch1[v] = 1
dfs.append(v)
DFS(0, v)
for x in dfs:
    print(x, end=" ")
print()


# BFS
bfs = []
ch2 = [0] * (n + 1)
Q = deque()
Q.append(v)
while Q:
    now = Q.popleft()
    if ch2[now] == 0:
        ch2[now] = 1
        bfs.append(now)
    for i in range(1, n + 1):
        if graph[now][i] == 1 and ch2[i] == 0:
            Q.append(i)
for x in bfs:
    print(x, end=" ")
