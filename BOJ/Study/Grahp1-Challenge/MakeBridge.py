# 다리 만들기

import sys
from collections import deque
sys.setrecursionlimit(100000)


n = int(sys.stdin.readline().rstrip())
Map = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
visit = [[0]*n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
Q = deque()
boundary = []
cnt = 1
# 먼저, 섬마다 경계 좌표를 구하여 각각 boundary 리스트에 저장한다.
for i in range(n):
    for j in range(n):
        if Map[i][j] == 1 and visit[i][j] == 0:
            visit[i][j] = cnt
            tmp = set()
            Q.append((i, j))
            while Q:
                t = Q.popleft()
                for k in range(4):
                    xx = t[0] + dx[k]
                    yy = t[1] + dy[k]
                    if 0 <= xx < n and 0 <= yy < n:
                        if Map[xx][yy] == 1 and visit[xx][yy] == 0:
                            visit[xx][yy] = cnt
                            Q.append((xx, yy))
                        elif Map[xx][yy] == 0:  # 섬의 경계 좌표
                            tmp.add((t[0], t[1]))
            boundary.append(list(tmp))
            cnt += 1
res = 2147000000
for i in range(len(boundary)):
    start = i + 1
    for j in boundary[i]:
        visit2 = [[0] * n for _ in range(n)]
        L = 0
        flag = False
        Q1 = deque()
        Q1.append((j[0], j[1]))
        while Q1:
            if flag:
                break
            if L-1 >= res:
                break
            size = len(Q1)
            for _ in range(size):
                t1 = Q1.popleft()
                if visit[t1[0]][t1[1]] != 0 and visit[t1[0]][t1[1]] != start:  # 다른 섬을 만나는 경우
                    res = min(res, L-1)
                    flag = True
                    break
                for k in range(4):
                    xx = t1[0] + dx[k]
                    yy = t1[1] + dy[k]
                    if 0 <= xx < n and 0 <= yy < n:
                        if visit[xx][yy] == start:
                            continue
                        if visit2[xx][yy] == 0 or (visit[xx][yy] != 0 and visit[xx][yy] != start):  # 바다인 경우와 다른 섬인 경우의 좌표를 Q에 push
                            visit2[xx][yy] = 1
                            Q1.append((xx, yy))
            L += 1
print(res)