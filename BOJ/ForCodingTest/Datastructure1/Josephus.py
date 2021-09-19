# 조세퍼스 문제

# 시간 6000ms
# import sys
# from collections import deque
# n, k = map(int, sys.stdin.readline().rstrip().split())
# Q = deque(i for i in range(1, n+1))
# res = []
# cnt = 1
# while Q:
#     tmp = Q.popleft()
#     if cnt == k:
#         res.append(tmp)
#         cnt = 1
#     else:
#         Q.append(tmp)
#         cnt += 1
# print('<', end="")
# for i in range(n):
#     print(res[i], end="")
#     if i != n-1:
#         print(", ", end="")
# print('>')

# 요세푸스 문제
# 시간 72ms
import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
stack = [i for i in range(1, n+1)]
res = []
tk = k-1
tn = n
while stack:
    tmp = stack.pop(tk % tn)
    res.append(tmp)
    tn -= 1
    if tn == 0:
        continue
    tk += k-1
    tk %= tn
print("<", end="")
for i in range(n-1):
    print(res[i], end=", ")
print(res[n-1], end=">")