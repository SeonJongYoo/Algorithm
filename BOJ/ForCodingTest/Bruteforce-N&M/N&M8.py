# N과 M 8

import sys


def DFS(L, s):
    if L == m:
        for x in res:
            print(x, end=" ")
        print()
    else:
        for i in range(s, n):
            res.append(arr[i])
            DFS(L+1, i)
            res.pop()


n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
res = []
DFS(0, 0)