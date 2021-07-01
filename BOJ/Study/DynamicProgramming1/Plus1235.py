# 1, 2, 3, 더하기 5

# import sys
#
# dp = [0]*100001
# dp[0] = 1
# dp[1] = 1
# dp[2] = 1
# dp[3] = 3
# for i in range(4, 10):
#     # 1이 오른쪽에 올 때
#     print("i: ", i)
#     t1 = dp[i-1]
#     tmp = dp[i-2]
#     k = 3
#     while k < i-1:  # d[6] = dp[5] - (dp[4] - dp[3] - dp[2])
#         tmp -= dp[i-k]
#         k += 1
#     t1 -= tmp
#     print("1:", t1, end=", ")
#
#     # 2가 오른쪽에 올 때
#     t2 = dp[i-2]
#     tmp = dp[i-4]
#     k = 6
#     while k < i:
#         tmp -= dp[i-k]
#         k += 2
#     t2 -= tmp
#     print("2:", t2, end=", ")
#
#     # 3이 오른쪽에 올 때
#     t3 = dp[i - 3]
#     if i > 5:
#         tmp = dp[i - 6]
#         k = 9
#         while k < i:
#             tmp -= dp[i - k]
#             k += 3
#         t3 -= tmp
#     print("3: ", t3)
#     dp[i] = t1 + t2 + t3
#     print("dp: ", dp[i])
#     print("----------------")
#t = int(sys.stdin.readline().rstrip())

# dp[1] 1 -> (1 1) -> 0
# dp[0] 2 -> 2 -> 1

# dp[2] 1 -> 2 1 -> 1
# dp[1] 2 -> 1 2 -> 1
# dp[0] 3 -> 3 -> 1

# dp[3] 1 -> (2 1 1), 1 2 1, 3 1 -> 2
# dp[2] 2 -> (2 2) -> 0
# dp[1] 3 -> 1 3 -> 1

# dp[4] 1 -> (1 2 1 1), (3 1 1), 1 3 1 -> 1
# dp[3] 2 -> (1 2 2), 2 1 2, 3 2 -> 2
# dp[2] 3 -> 2 3 -> 1

# dp[5] 1 -> 2 1 2 1, 3 2 1, 2 3 1 -> 3
# dp[4] 2 -> 3
# dp[3] 3 -> 2


import sys

dp = [[0]*100001 for _ in range(4)]
dp[1][1] = 1
dp[2][1] = 0
dp[3][1] = 0
dp[1][2] = 0
dp[2][2] = 1
dp[3][2] = 0
dp[1][3] = 1
dp[2][3] = 1
dp[3][3] = 1

for i in range(4, 100001):
    # 1이 오른쪽에 올 때
    dp[1][i] = dp[2][i-1]%1000000009 + dp[3][i-1]%1000000009
    # 2가 오른쪽에 올 때
    dp[2][i] = dp[1][i-2]%1000000009 + dp[3][i-2]%1000000009
    # 3이 오른쪽에 올 때
    dp[3][i] = dp[1][i-3]%1000000009 + dp[2][i-3]%1000000009

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    print((dp[1][n] + dp[2][n] + dp[3][n])%1000000009)