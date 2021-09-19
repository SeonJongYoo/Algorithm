# 카잉 달력


# 첫 번째 풀이 - 시간초과
# import sys
#
# t = int(sys.stdin.readline().rstrip())
# for _ in range(t):
#     m, n, x, y = map(int, sys.stdin.readline().rstrip().split())
#     sx, sy = 1, 1
#     year = 1
#     if m == n:
#         if x == y:
#             print(x)
#         else:
#             print(-1)
#     else:
#         while True:
#             sx += 1
#             sy += 1
#             year += 1
#             if sx > m:
#                 sx = 1
#             if sy > n:
#                 sy = 1
#             if sx == x and sy == y:
#                 print(year)
#                 break
#             if sx == 1 and sy == 1:
#                 print(-1)
#                 break
#             print(sx, sy, year)


# 시간초과
# import sys
#
# t = int(sys.stdin.readline().rstrip())
# for _ in range(t):
#     m, n, x, y = map(int, sys.stdin.readline().rstrip().split())
#     year = 1
#     while True:
#         if (year-x)%m == 0 and (year-y)%n == 0:
#             print(year)
#             break
#         elif (year-m)%m == 0 and (year-n)%n == 0:
#             print(-1)
#             break
#         year += 1


# 정답 코드
# x를 고정하고 y만 이동시켜 정답을 찾는다.
# 나머지 연산을 이용한 숫자 다루기
import sys
from math import gcd

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().rstrip().split())
    # m과 n의 최소공배수가 마지막 해이다.
    Max = int(m*n/gcd(m, n))
    res = 0
    for year in range(x, Max+1, m):  # x를 고정시키고 y를 찾는다. \
        if (year-y) % n == 0:
            res = year
            break
    if res:
        print(res)
    else:
        print(-1)