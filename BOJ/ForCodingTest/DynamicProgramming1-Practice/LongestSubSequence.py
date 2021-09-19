# 가장 긴 감소하는 부분 수열

import sys

n = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
A.insert(0, 0)
dp = [0]*(n+1)
dp[1] = 1
for i in range(2, n+1):
    Max = 0
    for j in range(1, i):
        if A[i] < A[j] and dp[j] > Max:
            Max = dp[j]
    dp[i] = Max + 1
print(max(dp[1:]))