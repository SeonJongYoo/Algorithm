# 사과나무(BFS) - chapter2 탐색&시뮬레이션에서 다룬 문제


# 내가 작성한 코드
from collections import deque
n = int(input())
arr = []
for i in range(n):
    num = list(map(int, input().split()))
    arr.append(num)
cnt, row = 0, 0
dQ = deque()
dQ.append(arr[row][n//2])
while True:
    while dQ:
        cnt += dQ.popleft()
    row += 1
    if row > n-1:
        break
    if row <= n//2:
        for j in range(n//2-row, n//2+row+1):
            dQ.append(arr[row][j])
    else:
        tmp = row - n//2
        for j in range(tmp, n-tmp):
            dQ.append(arr[row][j])
print(cnt)


# 강의 코드
# 상태트리 구성하기
# B(L): 주어진 이차원 리스트에서 중점부터 시작한다. (n//2, n//2)부터 시작하여 탐색을 진행한다.
# 좌표를 중심으로 위, 오른쪽, 아래, 왼쪽으로 총 4개의 edge를 형성한다.
# L = 0: (2, 2) --> L = 1: (1, 2), (2, 3), (3, 2), (2, 1) ---> L = 2: ...
# 방문했던 곳을 체크하기 위한 ch리스트를 선언한다.
from collections import deque
# ***********************************
# dx, dy는 좌표의 위(0, -1), 오른쪽(1, 0), 아래(0, 1), 왼쪽(-1, 0)을 나타내기 위한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# ***********************************
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ch = [[0] * n for _ in range(n)]  # 좌표를 방문했는지 체크하기 위한 리스트
Sum = 0
Q = deque()
ch[n//2][n//2] = 1  # 시작 좌표 = (n//2, n//2)는 미리 체크해둔다.
Sum += a[n//2][n//2]
Q.append((n//2, n//2))  # 좌표 자체를 큐에 삽입한다.
L = 0  # 상태트리의 Level을 나타냄
while True:
    if L == n//2:  # 이차원 리스트의 중점 좌표에서 시작하므로 주어진 리스트 크기의 절반이 종료 지점이 된다.
        break
    size = len(Q)  # 처음엔 size가 1
    for i in range(size):
        tmp = Q.popleft()  # tmp엔 좌표가 저장됨
        for j in range(4):
            x = tmp[0] + dx[j]
            y = tmp[1] + dy[j]
            if ch[x][y] == 0:
                Sum += a[x][y]
                ch[x][y] = 1
                Q.append((x, y))
    L += 1