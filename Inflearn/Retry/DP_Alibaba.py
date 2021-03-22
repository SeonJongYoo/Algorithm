# 알리바바 - BottompUp
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dy = [[0]*(n+1) for _ in range(n+1)]
dy[0][0] = arr[0][0]
# 이전 위치의 에너지 합(dy)과 현재 위치의 에너지(arr)를 더해서 최솟값을 dy리스트에 저장한다.
for i in range(1, n+1):
    for j in range(1, n+1):
        if dy[i-1][j] == 0:
            dy[i][j] += arr[i-1][j-1] + dy[i][j-1]
        elif dy[i][j-1] == 0:
            dy[i][j] += arr[i-1][j-1] + dy[i-1][j]
        else:
            dy[i][j] += arr[i-1][j-1] + min(dy[i - 1][j], dy[i][j-1])

print(dy[n][n])

# 알리바바 - TopDown
def DFS(x, y):
    if dy[x][y] > 0:  # 이미 존재하는 값의 경우 바로 찾아서 return한다.
        return dy[x][y]
    if x == 0 and y == 0:  # 직관적으로 구할 수 있는 값!
        return arr[0][0]
    else:
        # x == 0 또는 y == 0일 때 arr리스트의 index 범위를 벗어나므로 반대의 경우만 더해주면 된다.
        if x == 0:
            dy[x][y] = arr[x][y] + DFS(x, y-1)
        elif y == 0:
            dy[x][y] = arr[x][y] + DFS(x-1, y)
        else:
            dy[x][y] = arr[x][y] + min(DFS(x-1, y), DFS(x, y-1))
            return dy[x][y]


if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dy = [[0] * n for _ in range(n)]
    dy[0][0] = arr[0][0]
    for i in range(1, n):
        dy[0][i] = dy[0][i-1] + arr[0][i]
        dy[i][0] = dy[i-1][0] + arr[i][0]
    DFS(n-1, n-1)
    #for i in range(n):
    #    for j in range(n):
    #        print(dy[i][j], end=' ')
    #    print()
    print(dy[n-1][n-1])