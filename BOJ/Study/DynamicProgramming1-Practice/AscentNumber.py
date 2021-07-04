# 오르막 수

import sys

n = int(sys.stdin.readline().rstrip())
dp = [[0]*1001 for _ in range(10)]
div = 10007
# dp[x][y]: 수의 길이가 y이고 x로 끝나는 오르막 수의 개수
for i in range(10):
    dp[i][1] = 1
for i in range(2, 1001):
    for j in range(10):
        for k in range(j+1):
            dp[j][i] += dp[j-k][i-1]%div
res = 0
for i in range(10):
    res += dp[i][n]
print(res%div)