# 알리바바와 40인의 도둑(Top-Down) - 재귀 사용

# 내가 작성한 코드
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dy = [[0]*N for _ in range(N)] # memoization을 위해 필요
dy[0][0] = arr[0][0]
for i in range(N):
    dy[0][i] = dy[0][i-1] + arr[0][i]
    dy[i][0] = dy[i-1][0] + arr[i][0]

def DFS(n, m):
    if dy[n][m] > 0:
        return dy[n][m]
    if n > 0 and m > 0:
        dy[n][m] = min(DFS(n, m-1), DFS(n-1, m)) + arr[n][m] # memoization 과정
        return dy[n][m]
    else:
        if n == 0 and m > 0:
            dy[n][m] = min(DFS(n, m - 1), DFS(n - 1, m)) + arr[n][m] # memoization 과정
        elif m == 0 and n > 0:
            dy[n][m] = min(DFS(n, m - 1), DFS(n - 1, m)) + arr[n][m] # memoization 과정
        return dy[n][m]

print(DFS(N-1, N-1))

# 강의 코드
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dy = [[0]*N for _ in range(N)] # memoization을 위해 필요
def DFS(x, y):
    if dy[x][y] > 0:
        return dy[x][y]
    if x == 0 and y == 0:
        return dy[0][0]
    else:
        if y == 0: # 0열에 해당함
            dy[x][y] = DFS(x-1, y) + arr[x][y]  # memoization 과정
        elif x == 0:# 0행에 해당함
            dy[x][y] = DFS(x, y-1) + arr[x][y] # memoization 과정
        else: # 0열에 해당하지 않고 0행에도 해당하지 않는 경우. 현재 위치에서 위 또는 아래에서 최솟값을 찾는다.
            dy[x][y] = min(DFS(x-1, y), DFS(x, y-1)) + arr[x][y] # memoization 과정
        return dy[x][y]

print(DFS(N-1, N-1))

