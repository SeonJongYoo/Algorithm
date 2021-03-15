# 송아지 찿기(BFS: 상태트리 탐색)


# 강의 코드
from collections import deque
Max = 10000
ch = [0] * (Max+1)  # 좌표를 지나면 해당 좌표를 지났다고 1로 체크한다.
dis = [0] * (Max+1)  # 현재 좌표에서 특정 좌표까지 이동한 횟수를 기록한다.
n, m = map(int, input().split())
ch[n] = 1  # 출발점 체크
dis[n] = 0  # 출발점은 0
dQ = deque()
dQ.append(n)
while dQ:
    now = dQ.popleft()
    if now == m:  # 도착지점을 발견하면 바로 break
        break
    for next in (now-1, now+1, now+5):  # for문이 tuple의 각 원소들을 모두 확인하기 위해 3번 돌게됨
        if 0 < next <= Max:
            if ch[next] == 0:
                dQ.append(next)
                ch[next] = 1
                dis[next] = dis[now] + 1
print(dis[m])