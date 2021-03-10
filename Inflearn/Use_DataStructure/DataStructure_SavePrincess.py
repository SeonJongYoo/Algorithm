#  공주 구하기(큐)

# deque 이용 - append, popleft
# 내가 작성한 코드
from collections import deque

n, k = map(int, input().split())
dq = list(range(1, n+1))
dq = deque(dq)
cnt = 1
while len(dq) > 1:
    if cnt == k:
        dq.popleft()
        cnt = 1
    else:
        a = dq.popleft()
        dq.append(a)
        cnt += 1
print(dq[0])

# 강의 코드
n, k = map(int, input().split())
dq = list(range(1, n+1))
dq = deque(dq)
while dq:
    for _ in range(k-1):  # k-1번째까지는 popleft, append 진행
        cur=dq.popleft()
        dq.append(cur)
    dq.popleft()  # k번째에서는 popleft!
    if len(dq) == 1:
        print(dq[0])
        dq.popleft()
