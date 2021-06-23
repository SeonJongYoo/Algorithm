# 123 더하기 4


# 중복이 제거되어야 한다.
import sys
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    dp = [[0]*(n+1) for _ in range(4)]
    dp[1][1] = 1
    dp[1][2] = 1
    dp[2][2] = 1
    dp[1][3] = 1
    dp[2][3] = 1  # 식이 2로 시작 -> 3-2 = 1을 만드는 경우의 수를 구하면 된다. 2이하의 숫자들을 사용하여 3을 만드는 경우의 수
    dp[3][3] = 1  # 식이 3으로 시작 -> 3-3 = 0을 만드는 경우의 수를 구하면 된다. 3이하의 숫자들을 사용하여 3을 만드는 경우의 수
    for i in range(4, n+1):
        dp[1][i] = dp[1][i-1]  # 식이 1로 시작하는 경우 -> i-1을 만드는 경우의 수를 구한다.
        dp[2][i] = dp[1][i-2] + dp[2][i-2]  # 식이 2로 시작하는 경우 -> i-2를 만드는 경우의 수
        dp[3][i] = dp[1][i-3] + dp[2][i-3] + dp[3][i-3]  # 식이 3으로 시작하는 경우 -> i-3을 만다는 경우의 수
    for i in range(1, 4):
        for j in range(1, n+1):
            print(dp[i][j], end=" ")
        print()
    print("-------------------")
    print(dp[1][n] + dp[2][n] + dp[3][n])
