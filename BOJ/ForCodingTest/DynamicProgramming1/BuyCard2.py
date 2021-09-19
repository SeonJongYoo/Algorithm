# 카드 구매하기 2

import sys
n = int(sys.stdin.readline().rstrip())
p = list(map(int, sys.stdin.readline().rstrip().split()))
p.insert(0, 0)
dp = [0]*(n+1)
dp[1] = p[1]
for i in range(2, n+1):
    k = 0
    while k < i:
        if dp[i] == 0:
            dp[i] = dp[k] + p[i-k]
        else:
            dp[i] = min(dp[i], dp[k] + p[i-k])
        k+=1
print(dp[n])
