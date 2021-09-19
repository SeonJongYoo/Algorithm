# 연속합


# 내가 작성한 코드 - 메모리 초과
# import sys
# n = int(sys.stdin.readline().rstrip())
# A = list(map(int, sys.stdin.readline().rstrip().split()))
# A.insert(0, 0)
# dp = [[0]*(n+1) for _ in range(n+1)]
# # dp[x][y]: A[y]가 수열의 끝에 오고 총 x개의 숫자들을 사용했을 때 합
# dp[1][1] = A[1]
# dp[1][2] = A[2]
# dp[2][2] = dp[1][1] + A[2]
# for i in range(3, n+1):
#     for j in range(1, i+1):
#         dp[j][i] = dp[j-1][i-1] + A[i]
# Max = -1000000000
# k = 1
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(dp[i][j], end=" ")
#         if dp[i][j] > Max:
#             Max = dp[i][j]
#     #k += 1
#     print()
# print(Max)


import sys
n = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
A.insert(0, 0)
dp = [0]*(n+1)
dp[1] = A[1]
for i in range(2, n+1):
    dp[i] = max(dp[i-1] + A[i], A[i])
print(max(dp[1:]))
