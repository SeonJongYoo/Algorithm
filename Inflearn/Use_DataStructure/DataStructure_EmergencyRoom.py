# 응급실

# 환자들 간의 위험도가 같은 경우를 생각하면서 구현해야함!

# 내가 작성한 코드
# 환자들의 위험도만 고려하여 구현하였을 때, 위험도가 같은 환자들 끼리의 구분이 없어서 에러 발생!
from collections import deque

n, m = map(int, input().split())
danger = list(map(int, input().split()))
danger = deque(danger)  # 환자들의 위험도를 담고 있는 큐
dgIndex = list(range(n))
dgIndex = deque(dgIndex)  # 환자들의 index를 담고 있는 큐
mPatient = danger[m]  # m번째 환자의 위험도
cnt = 0
while m in dgIndex:
    dg = danger[0]
    if dg < max(danger):
        tmp = danger.popleft()
        danger.append(tmp)
        tmp1 = dgIndex.popleft()
        dgIndex.append(tmp1)
    else:
        danger.popleft()
        dgIndex.popleft()
        cnt += 1
print(cnt)

# 강의 코드
n, m = map(int, input().split())
Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q = deque(Q)
# 환자의 순번(index)와 위험도를 튜플로 표현함
cnt = 0
while True:
    cur = Q.popleft()  # 맨 앞의 환자를 pop하고 남은 환자들의 위험도와 비교
    if any(cur[1] < x[1] for x in Q):  # any() 함수: 인자중에 하나라도 참이면 True return!
        Q.append(cur)   # 현재 환자보다 남은 환자 중 더 높은 위험도가 있으면 현재 환자를 Q에 append
    else:  # 현재 진료를 받게 되는 환자
        cnt += 1
        if cur[0] == m:  # 환자의 순번을 확인
            print(cnt)
            break