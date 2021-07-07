# N과 M 5


import sys


def DFS(L):
    if L == m:
        for x in res:
            print(x, end=" ")
        print()
    else:
        for i in range(n):
            if visit[i] == 0:
                visit[i] = 1
                res.append(arr[i])
                DFS(L+1)
                visit[i] = 0
                res.pop()


n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
res = []
visit = [0]*n
DFS(0)