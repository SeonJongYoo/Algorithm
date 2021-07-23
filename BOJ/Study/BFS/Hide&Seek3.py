# 숨바꼭질 3


# 0-1 BFS 알고리즘
# 순간이동을 할 때는 앞뒤 이동과 달리 걸리는 시간이 0초이다.
# 즉, 이는 순간이동 할 때의 가중치가 0이고 앞뒤 이동 시의 가중치가 1을 의미한다.
import sys
from collections import deque


n, k = map(int, sys.stdin.readline().rstrip().split())
Q = deque()
visit = [-1]*100001
visit[n] = 0
Q.append(n)
while Q:
    size = len(Q)
    for _ in range(size):
        curr = Q.popleft()
        if curr == k:
            print(visit[k])
            sys.exit(0)
        x1 = curr * 2
        x2 = curr - 1
        x3 = curr + 1
        # 가장 먼저 가중치가 0인 순간이동부터 방문 처리한다.
        # 이유: visit 리스트에는 현재 위치에서 다른 위치로 이동 시 이전에 방문했던 곳이라면
        # 다시 방문하지 않는다. 따라서, 처음 방문했을 때 최소로 걸린 시간을 기록해줘야 한다.
        if 0 <= x1 < 100001 and visit[x1] == -1:
            visit[x1] = visit[curr]
            Q.append(x1)
        if 0 <= x2 < 100001 and visit[x2] == -1:
            visit[x2] = visit[curr] + 1
            Q.append(x2)
        if 0 <= x3 < 100001 and visit[x3] == -1:
            visit[x3] = visit[curr] + 1
            Q.append(x3)
