# 최대 선 연결하기

#내가 작성한 코드(강의 코드와 동일)
N = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
dy = [0]*(N+1)
dy[1] = 1

for i in range(2, N+1):
    max_len = 0
    for j in range(i - 1, 0, -1):
        if arr[j] < arr[i] and dy[j] > max_len:
            max_len = dy[j]
    dy[i] = max_len + 1

print(max(dy))