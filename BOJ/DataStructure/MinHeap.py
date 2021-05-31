# 최소힙
import time
import heapq as hq
import sys

tree = []
n = int(sys.stdin.readline())
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(tree) == 0:
            print(0)
        else:
            print(hq.heappop(tree))
    else:
        hq.heappush(tree, x)
