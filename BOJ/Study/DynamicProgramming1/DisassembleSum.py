# 합분해

# import sys
# n, k = map(int, sys.stdin.readline().rstrip().split())
# dp = [[0]*(n+1) for _ in range(k+1)]
# # dp[x][y]: x개의 숫자들을 합하여 y를 만드는 경우의 수
# for i in range(1, n+1):
#     dp[1][i] = 1
# #dp[2][1] = 2 -> 2개의 숫자들을 합하여 1을 만드는 경우의 수
# # 1 + 0, 0 + 1
# if k == 1:
#     print(1)
# else:
#     for i in range(1, n+1):
#         for j in range(2, k+1):
#             dp[j][i] = dp[j-1][i]

import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
dp = [[0]*(n+1) for _ in range(n+1)]
# dp[x][y]: x가 맨 오른쪽에 올 때 숫자들을 합하여 y를 만드는 경우의 수

# 1 + 0, 0 + 1
if k == 1:
    print(1)
else:
    for i in range(1, n+1):
        for j in range(2, k+1):
            dp[j][i] = dp[j-1][i]