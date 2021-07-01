# 쉬운 계단 수


import sys
n = int(sys.stdin.readline().rstrip())
dp = [[0]*(n+1) for _ in range(10)]
for i in range(1, 10):
    dp[i][1] = 1

# 10
# 21, (01)
# d[x][y]: 길이가 y이고 마지막 숫자로 x가 올 때 계산수의 개수
div = 1000000000
for i in range(2, n+1):
    for j in range(10):
        if j + 1 < 10:
            dp[j][i] += dp[j+1][i-1]%div
        if j - 1 >= 0:
            dp[j][i] += dp[j-1][i-1]%div
res = 0
for i in range(10):
    res += dp[i][n]%div
print(res%div)