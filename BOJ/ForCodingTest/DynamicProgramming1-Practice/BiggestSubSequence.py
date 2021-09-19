# 가장 큰 증가 부분 수열

import sys

n = int(sys.stdin.readline().rstrip())
seq = list(map(int, sys.stdin.readline().rstrip().split()))
seq.insert(0, 0)
dp = [0]*(n+1)
dp[1] = seq[1]
for i in range(2, n+1):
    Max = 0
    for j in range(1, i):
        if seq[i] > seq[j] and dp[j] > Max:
            Max = dp[j]
    dp[i] = Max + seq[i]
print(max(dp[1:]))