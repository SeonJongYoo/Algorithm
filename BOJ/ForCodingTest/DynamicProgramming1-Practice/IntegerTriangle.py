# 정수 삼각형


# 가장 큰 부분 증가수열의 논리를 참고
import sys

n = int(sys.stdin.readline().rstrip())
triangle = [[0]]
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    triangle.append(tmp)
dp = [[-1]*n for _ in range(n+1)]
dp[1][0] = triangle[1][0]
for i in range(2, n+1):
    for j in range(i):
        if i == 0:
            dp[i][j] = dp[i-1][j] + triangle[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
print(max(dp[n]))