# 오큰수


# 내가 작성한 코드 - 시간 초과
# 원인: 16번 라인에서 brute force 탐색을 진행함
# import sys
# from collections import deque
# n = int(sys.stdin.readline().rstrip())
# A = deque(map(int, sys.stdin.readline().rstrip().split()))
# while A:
#     tmp = A.popleft()
#     flag = False
#     if not A:
#         print(-1, end=" ")
#         break
#     for x in A:
#         if tmp < x:
#             flag = True
#             print(x, end=" ")
#             break
#     if not flag:
#         print(-1, end=" ")


# 내가 작성한 코드2 - 성공
# 배열의 역순을 구하는 a[::-1]는 시간 복잡도가 크다
import sys
n = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
stack = [A.pop()]
res = [-1]
while A:
    tmp = A.pop()
    if tmp >= stack[len(stack)-1]:
        for i in range(len(stack)-1, -1, -1):
            if tmp < stack[i]:
                res.append(stack[i])
                break
            else:
                stack.pop()
        if not stack:
            res.append(-1)
    else:
        res.append(stack[len(stack)-1])
    stack.append(tmp)
for i in res[::-1]:
    print(i, end=" ")


