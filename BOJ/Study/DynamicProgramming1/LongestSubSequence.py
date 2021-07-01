# 가장 긴 증가하는 부분 수열


# import sys
# n = int(sys.stdin.readline().rstrip())
# A = list(map(int, sys.stdin.readline().rstrip().split()))
# A.insert(0, 0)
# dp = [0]*(n+1)
# dp[1] = 1
# Max = A[1]
# Max_Length = dp[1]
# for i in range(2, n+1):
#     if A[i] > Max:
#         Max = A[i]
#         Max_Length += 1
#         dp[i] = Max_Length
#     else:
#         if A[i] > A[i-1]:
#             dp[i] = dp[i-1] + 1
#         else:
#             dp[i] = 1
# print(dp[1:n+1])


import sys
n = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
A.insert(0, 0)
dp = [0]*(n+1)
dp[1] = 1
# dp[i]: A[i]가 수열의 맨 마지막에 올 때 수열의 최대 길이
# i번째 숫자 앞에 1개가 오는 경우, 2개 오는 경우, i-1개가 오는 경우를 비교하여 최대 길이를 계산해야 한다.
for i in range(2, n+1):
    Max = 0
    for j in range(1, i):
        if A[i] > A[j] and dp[j] > Max:
            Max = dp[j]
    dp[i] = Max + 1
#print(dp[1:n+1])
print(max(dp))