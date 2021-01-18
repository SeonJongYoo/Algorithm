# 최대 부분 증가수열(LIS)

# 내가 작성한 코드
N = int(input())
arr = list(map(int, input().split()))
dy = [0] * (N + 1)
dy[0] = 1
for i in range(1, N):
    for j in range(i - 1, -1, -1):
        if arr[i] > arr[j] and dy[j] + 1 >= dy[i]:
            dy[i] = dy[j] + 1
        elif arr[i] < arr[j] and dy[i] < 1:
            dy[i] = 1
print(max(dy))

# 강의 코드
n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
dy = [0] * (n + 1)
dy[1] = 1
for i in range(2, n + 1):
    max_len = 0
    for j in range(i - 1, 0, -1):
        if arr[j] < arr[i] and dy[j] > max_len:  # arr[i]는 내가 만들고자 하는 LIS의 마지막 항
            max_len = dy[j]
    dy[i] = max_len + 1
print(max(dy))