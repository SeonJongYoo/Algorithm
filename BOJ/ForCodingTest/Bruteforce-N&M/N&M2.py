# N과 M 2

import sys


def DFS(L, s):
    if L == m:
        for j in range(1, n+1):
            if visit[j] == 1:
                print(j, end=" ")
        print()
    else:
        for i in range(s, n+1):
            if visit[i] == 0:
                visit[i] = 1
                DFS(L+1, i+1)
                visit[i] = 0


n, m = map(int, sys.stdin.readline().rstrip().split())
visit = [0]*(n+1)
DFS(0, 1)