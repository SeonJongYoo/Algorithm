# 로또

import sys


def DFS(L, s):
    if L == 6:
        for x in arr:
            print(x, end=" ")
        print()
    else:
        for i in range(s, inp[0]+1):
            arr.append(inp[i])
            DFS(L+1, i+1)
            arr.pop()


while True:
    inp = list(map(int, sys.stdin.readline().rstrip().split()))
    if inp[0] == 0:
        break
    arr = []
    DFS(0, 1)
    print()