# 연속합 2


# 시간 초과
# import sys
#
# n = int(sys.stdin.readline().rstrip())
# A = list(map(int, sys.stdin.readline().rstrip().split()))
# stack = []
# L = len(A)
# A.insert(0, 0)
# Max = -1000000000
# dp = [0]*(n+1)
# dp[1] = A[1]
# for i in range(2, n+1):
#     dp[i] = max(dp[i-1]+A[i], A[i])
# Max = max(max(dp[1:]), Max)
# if n > 1:
#     dp = [0] * n
#     while L > 0:
#         tmp = A.pop(L)
#         dp[1] = A[1]
#         for i in range(2, n):
#             dp[i] = max(dp[i-1]+A[i], A[i])
#         Max = max(max(dp[1:]), Max)
#         A.insert(L, tmp)
#         L -= 1
# print(Max)


# 기존에 구한 dp 배열에서 숫자 하나를 다시 빼주는 방식은?
# import sys
#
# n = int(sys.stdin.readline().rstrip())
# A = list(map(int, sys.stdin.readline().rstrip().split()))
# least = min(A)
# L = len(A)
# A.insert(0, 0)
# Max = -1000000000
# dp = [0]*(n+1)
# dp[1] = A[1]
# for i in range(2, n+1):
#     dp[i] = max(dp[i-1]+A[i], A[i])
# Max = max(max(dp[1:]), Max)
# print(Max)
# if n > 1:
#     dp1 = [0]*(n+1)
#     while L > 0:
#         for i in range(n+1):
#             dp1[i] = dp[i]
#         dp1[L] = dp1[L-1]
#         if L < n:
#             for i in range(L+1, n+1):
#                 dp1[i] = max(dp1[i-1] + A[i], A[i])
#         print(dp1[1:])
#         Max = max(max(dp1[1:]), Max)
#         L -= 1
# print(Max)


# import sys
#
# n = int(sys.stdin.readline().rstrip())
# A = list(map(int, sys.stdin.readline().rstrip().split()))
# least = min(A)
# L = len(A)
# A.insert(0, 0)
# Max = -1000000000
# dp = [[0]*(i+1) for i in range(n+1)]
# dp[1][1] = A[1]
# for i in range(2, n+1):
#     tMax = -1000000000
#     for j in range(1, i):
#         if dp[i-1][j] > tMax:
#             tMax = dp[i-1][j]
#     dp[i][0] = tMax
#     dp[i][1] = A[i]
#     for j in range(2, i+1):
#         dp[i][j] = max(dp[i-1][j-1], dp[i-1][0]) + A[i]
# for i in range(1, n+1):
#     for j in range(i+1):
#         print(dp[i][j], end=" ")
#     print()


# 정답 코드
import sys

n = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
A.insert(0, 0)
dp = [[-1000000001]*(n+1) for _ in range(2)]
# dp[x][y]: A[y]가 마지막 위치에 올 때
# x == 0: 이것을 삭제한 경우 연속합의 최댓값
# x == 1: 이것을 삭제하지 않은 경우 연속합의 최댓값
dp[1][1] = A[1]
for i in range(2, n+1):
    dp[0][i] = max(dp[0][i-1] + A[i], dp[1][i-1])  # 값을 선택하지 않는 경우 - 이전 위치까지의 연속합의 최댓값과 이전 값을 제거한 경우 연속합의 최댓값
    dp[1][i] = max(dp[1][i-1] + A[i], A[i])  # 현재값을 선택하는 경우
res = -1000000000
for i in range(2):
    for j in range(1, n+1):
        if dp[i][j] > res:
            res = dp[i][j]
print(res)