# N과 M 7

import sys


def DFS(L):
    if L == m:
        for x in res:
            print(x, end=" ")
        print()
    else:
        for i in range(n):
            res.append(arr[i])
            DFS(L+1)
            res.pop()


n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
res = []
DFS(0)