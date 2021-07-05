# 일곱 난쟁이

import sys


def DFS(L, s):
    if L == 7:
        if sum(res) != 100:
            return
        res.sort()
        for j in res:
            print(j)
        sys.exit(0)
    else:
        for i in range(s, 9):
            res.append(dwarf[i])
            DFS(L+1, i+1)
            res.pop()


dwarf = []
for _ in range(9):
    dwarf.append(int(sys.stdin.readline().rstrip()))
res = []
DFS(0, 0)