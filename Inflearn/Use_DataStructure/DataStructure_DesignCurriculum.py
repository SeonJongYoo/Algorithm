# 교육과정 설계 - 큐

# 내가 작성한 코드
# 수업 설계: AKDEF와 현수의 설계: WOPASFKGHDEF 인 경우 에러 발생
# 교육과정 과목이 중복되는 경우 에러 발생
from collections import deque
curr = list(input())
curr = deque(curr)  # 교육과정을 나타내는 큐
n = int(input())
for i in range(n):
    hyeonsu = list(input())
    hyeonsu = deque(hyeonsu)  # 현수의 수업설계를 나타내는 큐
    tlist = list(range(len(hyeonsu)))
    tlist = deque(tlist)  # 현수의 수업설계 index를 담고 있음
    check = []  # 현수의 수업설계 중 교육과정과 일치한다면 check에 append!
    for x in range(len(curr)):
        for y in range(len(hyeonsu)):
            tmp = hyeonsu.popleft()
            tmp1 = tlist.popleft()
            if curr[x] == tmp:
                check.append(tmp1)
                break
            else:
                hyeonsu.append(tmp)
                tlist.append(tmp1)
    if max(check) == check[len(check)-1] and len(check) == len(curr):
        print('#{} YES'.format(i+1))
    else:
        print('#{} NO'.format(i+1))

# 강의 코드
# 수업 계획을 하나씩 읽으면서(popleft) 현재 수업이 교육 과정에 있다면 교육과정 큐에서 popleft
# 일치하지 않으면 그냥 지나친다.
# 교육과정 중 일부만 이수한다면 잘못된 수업설계이다.
need = list(input())  # 교육과정
n = int(input())
for i in range(n):
    plan = input()
    dq = deque(need)
    for x in plan:  # 현수의 수업계획을 하나씩 읽음
        if x in dq:  # 읽은 수업계획이 교육과정에 있다면
            if x != dq.popleft():  # 현재 읽은 수업계획(x)이 교육과정에 있지만 이수 순서가 맞지 않다면
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq) == 0:
            print("#%d YES" %(i+1))
        else:  # 교육과정 중 일부만 이수한 경우
            print("#%d NO" % (i + 1))