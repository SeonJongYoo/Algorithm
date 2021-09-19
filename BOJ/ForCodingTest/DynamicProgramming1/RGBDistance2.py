# RGB 거리 2

import sys

n = int(sys.stdin.readline().rstrip())
home = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
home.insert(0, [0])
dp = [[0]*3 for _ in range(n+1)]
dp[1][0] = home[1][0]
dp[1][1] = home[1][1]
dp[1][2] = home[1][2]
i0, i1, i2 = 1, 0, 0
for i in range(2, n+1):
    if i > 2 and i == n:
        idx0, idx1, idx2 = 2, 2, 1
        print(i0, i1, i2)
        if i0 == 2:
            idx0 = 1
        if i1 == 2:
            idx1 = 0
        if i2 == 1:
            idx2 = 0
        print(idx0, idx1, idx2)
        dp[i][0] = dp[i - 1][idx0] + home[i][0]
        dp[i][1] = dp[i - 1][idx1] + home[i][1]
        dp[i][2] = dp[i - 1][idx2] + home[i][2]
    else:
        if i == 2:  # 1번째에서 선택한 색상
            if dp[i-1][1] >= dp[i-1][2]:
                i0 = 2
            if dp[i-1][0] >= dp[i-1][2]:
                i1 = 2
            if dp[i-1][0] >= dp[i-1][1]:
                i2 = 1
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + home[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + home[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + home[i][2]
for i in range(1, n+1):
    for j in range(3):
        print(dp[i][j], end=" ")
    print()