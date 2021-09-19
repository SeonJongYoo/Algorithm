# N과 M 3

import sys


def DFS(L):
    if L == m:
        for j in res:
            print(j, end=" ")
        print()
    else:
        for i in range(1, n+1):
            res.append(i)
            DFS(L+1)
            res.pop()


n, m = map(int, sys.stdin.readline().rstrip().split())
res = []
DFS(0)