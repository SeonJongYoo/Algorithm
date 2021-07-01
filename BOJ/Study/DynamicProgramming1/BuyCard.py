# 카드 구매하기

import sys
n = int(sys.stdin.readline().rstrip())
p = list(map(int, sys.stdin.readline().rstrip().split()))
p.insert(0, 0)
dp = [0]*(n+1)
dp[1] = p[1]
for i in range(2, n+1):
    k = 0
    while k < i:
        dp[i] = max(dp[i], dp[k] + p[i-k])
        k += 1
print(dp[n])