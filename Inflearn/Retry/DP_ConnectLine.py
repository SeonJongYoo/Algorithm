# 최대 선 연결하기
# 최대 부분증가수열과 같은 문제
n = int(input())
arr = list(map(int, input().split()))
dy = [0] * n
dy[0] = 1
for i in range(1, n):
    Max = 0
    for j in range(i-1, -1, -1):
        if arr[i] > arr[j] and dy[j] > Max:
            Max = dy[j]
    dy[i] = Max + 1
print(max(dy))