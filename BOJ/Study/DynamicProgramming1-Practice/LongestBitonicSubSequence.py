# 가장 긴 바이토닉 부분 수열


# 실패 - 알고리즘이 틀린 것 같음
# import sys
#
# n = int(sys.stdin.readline().rstrip())
# A = list(map(int, sys.stdin.readline().rstrip().split()))
# A.insert(0, 0)
# dp = [0]*(n+1)
# dp[1] = 1
# for i in range(2, n+1):
#     Max = 0
#     value = 0
#     ck = False
#     for j in range(1, i):
#         if A[i] > A[j] and dp[j] > Max and not ck:
#             if A[j] > value:
#                 value = A[j]
#                 Max = dp[j]
#         elif A[i] < A[j] and dp[j] > Max:
#             Max = dp[j]
#             ck = True
#     dp[i] = Max + 1
# print(dp[1:])


# 정답
import sys

n = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
A.insert(0, 0)
dp = [[0]*(n+1) for _ in range(2)]
dp[0][1] = 1  # 가장 긴 증가하는 부분 수열 체크
dp[1][1] = 1  # 가장 긴 바이토닉 부분 수열 체크
for i in range(2, n+1):
    Max1, Max2 = 0, 0
    for j in range(1, i):
        if A[i] > A[j] and dp[0][j] > Max1:
            Max1 = dp[0][j]
            if dp[0][j] > Max2:
                Max2 = dp[0][j]
        elif A[i] < A[j] and dp[1][j] > Max2:
            Max2 = dp[1][j]
    dp[0][i] = Max1 + 1
    dp[1][i] = Max2 + 1

print(max(dp[1]))