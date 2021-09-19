# 알고스팟


# import sys
# from collections import deque
#
# m, n = map(int, sys.stdin.readline().rstrip().split())
# maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
# dx = [0, 1]
# dy = [1, 0]
# Q = deque()
# Q.append((0, 0))
# visit = [[0]*m for _ in range(n)]
# visit[0][0] = 1
# cnt = 0
# check_room = False
# check = deque()
# check.append(0)
# # 인접한 곳이 빈 방과 벽이라면 빈 방을 선택한다.
# while Q:
#     size = len(Q)
#     print(Q)
#     print(check)
#     print("cnt: ", cnt)
#     print("-------------")
#     for _ in range(size):
#         cur = Q.popleft()
#         check.popleft()
#         if cur[0] == n-1 and cur[1] == m-1:
#             print(cnt)
#             sys.exit(0)
#         for i in range(2):
#             xx = cur[0] + dx[i]
#             yy = cur[1] + dy[i]
#             if 0 <= xx < n and 0 <= yy < m and visit[xx][yy] == 0:
#                 if xx == n-1 and yy == m-1:
#                     check_room = True
#                     visit[xx][yy] = 1
#                     Q.append((xx, yy))
#                     check.append(0)
#                     break
#                 if maze[xx][yy] == 0:  # 빈 방을 발견한 경우
#                     check_room = True
#                     visit[xx][yy] = 1
#                     if 1 in check:
#                         Q.clear()
#                         check.clear()
#                     Q.append((xx, yy))
#                     check.append(0)
#                 if maze[xx][yy] == 1 and 0 not in check:
#                     visit[xx][yy] = 1
#                     Q.append((xx, yy))
#                     check.append(1)
#     if not check_room:
#         cnt += 1
#     else:
#         check_room = False


# 0-1 BFS
# 우선순위 큐를 생각하자
# 빈방으로의 이동은 0초, 벽을 부수는 경우는 1초 걸린 것으로 생각할 수 있다.
import sys
from collections import deque

m, n = map(int, sys.stdin.readline().rstrip().split())
maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
Q = deque()
Q.append((0, 0))
visit = [[-1]*m for _ in range(n)]
visit[0][0] = 0
# 인접한 곳이 빈 방과 벽이라면 빈 방을 선택한다.
while Q:
    size = len(Q)
    for _ in range(size):
        cur = Q.popleft()
        if cur[0] == n-1 and cur[1] == m-1:
            print(visit[n-1][m-1])
            sys.exit(0)
        for i in range(4):
            xx = cur[0] + dx[i]
            yy = cur[1] + dy[i]
            if 0 <= xx < n and 0 <= yy < m:
                if maze[xx][yy] == 0 and visit[xx][yy] == -1:
                    visit[xx][yy] = visit[cur[0]][cur[1]]
                    Q.appendleft((xx, yy))
                elif maze[xx][yy] == 1 and visit[xx][yy] == -1:
                    visit[xx][yy] = visit[cur[0]][cur[1]] + 1
                    Q.append((xx, yy))