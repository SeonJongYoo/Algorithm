# 송아지 찾기 - BFS
# 알고리즘 구성은 맞았으나 점프 횟수를 구하는 것은 실패
# ch 리스트가 필요한 이유: 이미 방문했던 좌표를 또 지나게 되면 최소 점프 횟수를 구할 수 없음
from collections import deque
s, e = map(int, input().split())
dx = [1, -1, 5]
Q = deque()
Q.append(s)
ch = [0] * 10001  # 해당 좌표를 지났다는 체크 리스트
dis = [0] * 10001
ch[s] = 1
dis[s] = 0  # 시작 위치부터 index까지의 점프 횟수
while Q:
    tmp = Q.popleft()
    if tmp == e:
        break
    for i in range(3):
        if 1 <= tmp + dx[i] <= 10000 and ch[tmp+dx[i]] == 0:
            ch[tmp+dx[i]] = 1
            dis[tmp+dx[i]] = dis[tmp] + 1  # 이전 index까지의 점프 횟수에 1을 더해준다.
            Q.append(tmp+dx[i])
print(dis[e])