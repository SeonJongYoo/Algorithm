# 점프


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if (i != n-1 or j != n-1) and dp[i][j] > 0 and board[i][j] != 0:
            if j+board[i][j] < n:
                dp[i][j+board[i][j]] += dp[i][j]
            if i+board[i][j] < n:
                dp[i+board[i][j]][j] += dp[i][j]
            # dp리스트에서 지나간 경로에 1씩 더해줌으로써 그 경로를 몇 번 지나쳤는지 알 수 있다.

            #    for b in range(n):
            #        print(dp[a][b], end=' ')
            #    print()
            #print("---------------------")
print(dp[n-1][n-1])
