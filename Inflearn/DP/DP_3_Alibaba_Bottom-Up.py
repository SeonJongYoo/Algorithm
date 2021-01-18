# 알리바바와 40인의 도둑(Bottom-Up)

# 내가 작성한 코드
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dy = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        min_value = 100000
        if min(dy[i-1][j], dy[i][j-1]) < min_value:
            if min(dy[i-1][j], dy[i][j-1]) is 0:
                min_value = max(dy[i-1][j], dy[i][j-1])
            else:
                min_value = min(dy[i-1][j], dy[i][j-1])
        dy[i][j] = min_value + arr[i-1][j-1]
print(dy)
print(dy[N][N])

# 강의 코드
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dy = [[0] * n for _ in range(n)]
dy[0][0] = arr[0][0] # 직관적으로 알 수 있는 값은 직접 초기화
# dy리스트의 0행과 0열은 직관적으로 초기화할 수 있음
for i in range(n):
    dy[0][i] = dy[0][i-1] + arr[0][i] # dy리스트의 0행을 직접 초기화
    dy[i][0] = dy[i-1][0] + arr[i][0] # dy리스트의 0열을 직접 초기화

for i in range(1, n):
    for j in range(1, n):
        dy[i][j] = min(dy[i][j-1], dy[i-1][j]) + arr[i][j]
print(dy[n-1][n-1])