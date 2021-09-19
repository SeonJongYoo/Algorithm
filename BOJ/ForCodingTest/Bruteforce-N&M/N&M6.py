# N과 M 6

import sys


def DFS(L, s):
    if L == m:
        for j in range(n):
            if visit[j] == 1:
                print(arr[j], end=" ")
        print()
    else:
        for i in range(s, n):
            if visit[i] == 0:
                visit[i] = 1
                DFS(L+1, i+1)
                visit[i] = 0


n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
visit = [0]*n
DFS(0, 0)