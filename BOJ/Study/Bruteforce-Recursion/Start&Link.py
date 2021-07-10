# 스타트와 링크


import sys
import itertools as it


def DFS(L, s):
    global Min
    if L == n//2:
        link = []
        for i in range(n):
            if i not in start:
                link.append(i)
        tstart = it.combinations(start, 2)
        tlink = it.combinations(link, 2)
        s1, l1 = 0, 0
        for x in tstart:
            s1 += S[x[0]][x[1]] + S[x[1]][x[0]]
        for x in tlink:
            l1 += S[x[0]][x[1]] + S[x[1]][x[0]]
        Min = min(Min, abs(s1-l1))
    else:
        for i in range(s, n):
            start.append(i)
            DFS(L+1, i+1)
            start.pop()


n = int(sys.stdin.readline().rstrip())
S = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
start = [0]
Min = 2147000000
DFS(1, 1)
print(Min)
