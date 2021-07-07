# N과 M 10

import sys


def DFS(L, s):
    if L == m:
        res = []
        for j in range(n):
            if visit[j] == 1:
                res.append(arr[j])
        ans.add(tuple(res))
    else:
        for i in range(s, n):
            if visit[i] == 0:
                visit[i] = 1
                DFS(L + 1, i+1)
                visit[i] = 0


n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
visit = [0]*n
ans = set()
DFS(0, 0)
ans = list(ans)
ans.sort()
for x in ans:
    for y in x:
        print(y, end=" ")
    print()