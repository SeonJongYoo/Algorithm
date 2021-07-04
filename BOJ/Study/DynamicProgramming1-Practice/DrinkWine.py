# 포도주 시식

# 정답 코드
import sys


n = int(sys.stdin.readline().rstrip())
wine = []
for _ in range(n):
    wine.append(int(sys.stdin.readline().rstrip()))
wine.insert(0, 0)
dp = [0]*(n+1)
dp[1] = wine[1]
if n > 1:
    dp[2] = wine[2] + wine[1]  # 포도주의 양이 항상 양수이므로 2번째 포도주까지 마셨을 때 최댓값은
    # 1, 2번째 포도주 양을 더한 값
    for i in range(3, n+1):
        # dp[i-2] + wine[i]  # 현재 포도주를 마시고 2번째 전 포도주까지 마셨을 때의 최댓값을 더하는 경우
        # dp[i-3] + wine[i-1] + wine[i]  # 현재 포도주와 이전 포도주(1번째 전)를 마시고 이전 포도주에서
        # 2번째 전 포도주(현재 포도주 기준 3번째 전)를 마셨을 때 최댓값을 더하는 경우
        # dp[i-1]: 현재 포도주를 마시지 않는 경우
        dp[i] = max(dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i], dp[i-1])
print(max(dp[1:]))