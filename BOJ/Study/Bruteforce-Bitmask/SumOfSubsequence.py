# 부분수열의 합

import sys


def DFS(L, Sum):
    global res
    if L == n:
        flag = False
        for i in range(n):
            if visit[i] == 1:
                flag = True
        if not flag:
            return
        if Sum == s:
            res += 1
    else:
        if visit[L] == 0:
            visit[L] = 1
            DFS(L+1, Sum + seq[L])
            visit[L] = 0
        DFS(L+1, Sum)


n, s = map(int, sys.stdin.readline().rstrip().split())
seq = list(map(int, sys.stdin.readline().rstrip().split()))
res = 0
visit = [0]*n
DFS(0, 0)
print(res)