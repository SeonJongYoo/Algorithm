# 미로의 최단거리 통로(BFS 활용)


# 내가 작성한 코드 - 정답
from collections import deque
a = [list(map(int, input().split())) for _ in range(7)]
ch = [[0]*7 for _ in range(7)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
Q = deque()
Q.append((0, 0))
a[0][0] = 2
L = 0
cnt = 0
# 도착할 수 없는 경우에 대한 구분이 필요함
while True:
    if a[6][6] == 2:
        break
    size = len(Q)
    if size == 0:
        L = -1
        break
    for i in range(size):
        tmp = Q.popleft()
        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if 0 <= x < 7 and 0 <= y < 7:
                if a[x][y] == 0:
                    Q.append((x, y))
                    a[x][y] = 2
    L += 1
print(L)

# 강의 코드
# 상태트리 구성하기
# B(L): L은 현재 좌표에서 한번 이동하여 갈 수 있는 좌표들을 나타냄.
# (0, 0)부터 상하좌우를 탐색하면서 진행된다.
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
board = [list(map(int, input().split())) for _ in range(7)]
dis = [[0] * 7 for _ in range(7)]
Q = deque()
Q.append((0, 0))
board[0][0] = 1
while Q:
    tmp = Q.popleft()
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if 0 <= x <= 6 and 0 <= y <= 6 and board[x][y] == 0:
            board[x][y] = 1  # 방문한 좌표는 1로 체크
            dis[x][y] = dis[tmp[0]][tmp[1]] + 1
            # 이전 좌표까지 방문한 횟수에 1을 더하여 현재 좌표까지 방문한 개수를 저장함
            Q.append((x, y))

if dis[6][6] == 0:
    print(-1)
else:
    print(dis[6][6])
