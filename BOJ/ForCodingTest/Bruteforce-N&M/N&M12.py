# N과 M 12

import sys


def DFS(L, s):
    if L == m:
        ans.add(tuple(res))
    else:
        for i in range(s, n):
            res.append(arr[i])
            DFS(L + 1, i)
            res.pop()

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
visit = [0]*n
res = []
ans = set()
DFS(0, 0)
ans = list(ans)
ans.sort()
for x in ans:
    for y in x:
        print(y, end=" ")
    print()