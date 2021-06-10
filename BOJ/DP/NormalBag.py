# 평범한 배낭
# 일차원 리스트 풀이 - 큰 무게부터 탐색하면 중복이 발생하지 않음
n, k = map(int, input().split())
bag = []
dp = [0]*(k+1)
for _ in range(n):
    w, v = map(int, input().split())
    bag.append((w, v))
bag.insert(0, (0, 0))
for i in range(1, n+1):
    for j in range(k, bag[i][0]-1, -1):
        dp[j] = max(dp[j-bag[i][0]] + bag[i][1], dp[j])
print(max(dp))

# 이차원 리스트 풀이 - 메모리 초과
n, k = map(int, input().split())
bag = []
dp = [[0]*(k+1) for _ in range(k+1)]
for _ in range(n):
    w, v = map(int, input().split())
    bag.append((w, v))
bag.insert(0, (0, 0))
for i in range(1, n+1):
    for j in range(1, k+1):
        dp[i][j] = dp[i-1][j]
    for j in range(bag[i][0], k+1):
        dp[i][j] = max(dp[i-1][j-bag[i][0]] + bag[i][1], dp[i][j])
print(dp[n][k])