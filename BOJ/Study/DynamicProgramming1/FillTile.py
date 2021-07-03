# 타일 채우기

import sys

n = int(sys.stdin.readline().rstrip())
dp = [0]*(n+1)
if n > 1:
    dp[2] = 3
    dp[4] =
    for i in range(6, n+1):
        if i%2 == 1:
            continue
        dp[i] = dp[i-1]
    print(dp[1:])
else:
    print(0)