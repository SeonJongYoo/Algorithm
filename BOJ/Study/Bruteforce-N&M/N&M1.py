# N과 M(1)

import sys


def DFS(L):
    if L == m:
        for x in res:
            print(x, end=" ")
        print()
    else:
        for i in range(1, n+1):
            if visit[i] == 0:
                visit[i] = 1
                res.append(i)
                DFS(L+1)
                res.pop()
                visit[i] = 0


n, m = map(int, sys.stdin.readline().rstrip().split())
visit = [0]*(n+1)
res = []
DFS(0)