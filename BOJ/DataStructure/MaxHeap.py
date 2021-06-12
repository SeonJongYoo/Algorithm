# 최대 힙

import heapq as hq
import sys


n = int(sys.stdin.readline().rstrip())
tree = []
for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if len(tree) == 0:
            print(0)
        else:
            print(-hq.heappop(tree))
    else:
        hq.heappush(tree, -x)

