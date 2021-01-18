# 침몰하는 타이타닉 - 그리디 알고리즘

# 내가 작성한 코드 - 몸무게가 가장 큰 사람을 먼저 보트에 태운다. 이때, 전체 승객의 몸무게를 조사하여
# 보트에 태울 수 있는 승객이면 같이 태운다.
# 처음에 하나의 보트에 2명 이하의 승객만 태울 수 있다는 조건을 고려하지 않고 구현
N, M = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
arr.sort()
while sum(arr) != 0:
    weight = M
    cal = 0
    #print(arr)
    for i in range(N-1, -1, -1):
        if cal == 2:
            break
        if arr[i] != 0 and weight >= arr[i]:
            weight = weight - arr[i]
            arr[i] = 0
            cal += 1
    cnt += 1
    #print(cnt)

print(cnt)

# 강의 코드 - 리스트를 사용하여 구현
# 몸무게가 가장 큰 사람과 보트를 같이 탈 수 있는 가능성은 몸무게가 가장 작은 사람이 높다.
n, limit = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
cnt = 0
while p:
    if len(p) == 1: # 승객이 한명 남으면 그냥 보트에 태워서 보내면 끝! 아래 연산을 수행하면 오류 발생
        cnt += 1
        break
    if p[0] + p[-1] > limit: # 가장 가벼운 사람과 가장 무거운 사람이 같이 탈 수 없다면 가장 무거운 사람을 태운다.
        p.pop()
        cnt += 1
    else: # 같이 탈 수 있다면 둘 다 보트에 태운다.
        p.pop(0) # 리스트의 맨 앞의 원소를 삭제
        p.pop()
        cnt += 1

print(cnt)

# 강의 코드 - deque를 사용하여 구현
from _collections import deque
n, limit = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
p = deque(p) # 리스트 p가 deque형으로 변경됨
cnt = 0
while p:
    print(p)
    if len(p) == 1: # 승객이 한명 남으면 그냥 보트에 태워서 보내면 끝! 아래 연산을 수행하면 오류 발생
        cnt += 1
        break
    if p[0] + p[-1] > limit: # 가장 가벼운 사람과 가장 무거운 사람이 같이 탈 수 없다면 가장 무거운 사람을 태운다.
        p.pop()
        cnt += 1
    else: # 같이 탈 수 있다면 둘 다 보트에 태운다.
        p.popleft() # deque의 맨 앞의 원소를 삭제
        p.pop()
        cnt += 1
    print(cnt)

print(cnt)