# 로봇 청소기
'''n, m = map(int, input().split())
r, c, td = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
res = 1
area[r][c] = 2
while True:
    flag = False
    # 회전하기 전에 상하좌우 모두 탐색하여 0이 있는지 확인
    for i in range(4):
        tr = r + dx[i]
        tc = c + dy[i]
        if area[tr][tc] == 0:
            flag = True
            break
    if flag:
        # 현재 방향에서 왼쪽 회전
        rr = r + dx[td]
        cc = c + dy[td]
        if td == 0:  # 회전 후 방향 변경
            td = 3
        else:
            td -= 1
        if area[rr][cc] == 0:
            res += 1
            area[rr][cc] = 2
            r, c = rr, cc
    else:
        # 후진
        if td != 0:
            tr = r + dx[td-1]
            tc = c + dy[td-1]
        else:
            tr = r + dx[3]
            tc = c + dy[3]
        if area[tr][tc] == 1:  # 후진 시 뒤가 벽인 경우
            break
        else:
            r, c = tr, tc

print(res)'''


# BFS
from collections import deque
n, m = map(int, input().split())
r, c, d = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
Q = deque()
Q.append((r, c))
area[r][c] = 2  # 청소 완료 표시
res = 1  # 청소하는 칸의 개수
while True:
    flag = False
    tmp = Q.popleft()
    # 청소할 칸이 있는지 탐색
    for _ in range(4):
        rr = tmp[0] + dx[d]
        cc = tmp[1] + dy[d]
        if d == 0:
            d = 3
        else:
            d -= 1
        if area[rr][cc] == 0:
            flag = True
            res += 1
            area[rr][cc] = 2
            Q.append((rr, cc))
            break
    # 동서남북 모두 청소할 칸이 없는 경우
    if not flag:
        # 후진하기
        td = 3  # 북쪽을 바라보는 경우
        if d != 0:  # 그 외 방향을 바라보는 경우
            td = d-1
        rr = tmp[0] + dx[td]
        cc = tmp[1] + dy[td]
        if area[rr][cc] == 1:  # 뒷쪽이 벽인 경우
            break
        else:
            Q.append((rr, cc))
print(res)


