# 1, 2, 3 더하기 - 브루트 포스

import sys


def DFS(N):
    if N < 0:
        return 0
    if N == 0:
        return 1
    if N == 1:
        return 1
    if N == 2:
        return 2
    else:
        res = DFS(N-1) + DFS(N-2) + DFS(N-3)
    return res


t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    ans = DFS(n)
    print(ans)