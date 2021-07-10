# 링크와 스타트

import sys
import itertools as it


def DFS(L, s, max_len):
    global Min
    if Min == 0:
        return
    if L == max_len:
        link = []
        for i in range(n):
            if i not in start:
                link.append(i)
        s1, l1 = 0, 0
        tstart = it.combinations(start, 2)
        for x in tstart:
            s1 += S[x[0]][x[1]] + S[x[1]][x[0]]
        tlink = it.combinations(link, 2)
        for x in tlink:
            l1 += S[x[0]][x[1]] + S[x[1]][x[0]]
        #print(s1, l1)
        Min = min(Min, abs(s1-l1))
        #print("---------------")
    else:
        for i in range(s, n):
            start.append(i)
            DFS(L+1, i+1, max_len)
            start.pop()


n = int(sys.stdin.readline().rstrip())
S = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
Min = 2147000000
start = []
length = n//2
while length > 1:
    DFS(0, 0, length)
    if Min == 0:
        break
    length -= 1
print(Min)