# 가장 높은 탑 쌓기

# 내가 작성한 코드
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dy = [0] * N
dy[0] = arr[0][1]

for i in range(1, N):
    max_len = 0
    for j in range(i-1, -1, -1):
        if arr[j][0] > arr[i][0] and arr[j][2] > arr[i][2] and dy[j] > max_len:
            max_len = dy[j]
        elif arr[j][0] < arr[i][0] and arr[j][2] < arr[i][2] and dy[j] > max_len:
            max_len = dy[j]
    dy[i] = max_len + arr[i][1]

print(dy)
print(max(dy))

# 수정한 코드
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# arr을 0번째 원소(밑면의 넓이)에 대하여 내림차순으로 정렬한다.
arr = sorted(arr, key=lambda x: -x[0])
dy = [0] * N
dy[0] = arr[0][1]

for i in range(1, N):
    max_len = 0
    for j in range(i-1, -1, -1):
        if arr[j][2] > arr[i][2] and dy[j] > max_len:
            max_len = dy[j]
    dy[i] = max_len + arr[i][1]

print(max(dy))
# 내림차순으로 정렬하여 비교 대상의 개수를 줄이는 것이 중요!!

# 강의 코드
import sys
sys.stdin = open("in1.txt", 'r')
if __name__ == "__main__":
    n = int(input())
    bricks = []
    for i in range(n):
        a, b, c = map(int, input().split())
        bricks.append((a, b, c)) # 벽돌의 정보를 튜플 형태로 리스트에 저장
    bricks.sort(reverse=True) # 각 벽돌을 밑면의 넓이에 대하여 내림차순으로 저장
    dy = [0] * n
    dy[0] = bricks[0][1]
    res = bricks[0][1]
    for i in range(1, n):
        max_h = 0
        for j in range(i-1, -1, -1):
            if bricks[j][2] > bricks[i][2] and dy[j] > max_h:
                max_h = dy[j]
        dy[i] = max_h + bricks[i][1]
        res = max(res, dy[i])
    print(res)