# 격자판 최대합

# 내가 작성한 코드
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
row = col = dia = 0

# 행 중에서 최댓값
for i in range(n):
    sum = 0
    for j in range(n):
        sum += arr[i][j]
    row = max(row, sum)

# 열 중에서 최댓값
for i in range(n):
    sum = 0
    for j in range(n):
        sum += arr[j][i]
    col = max(col, sum)

# 두 대각선 중 최댓값
sum1 = sum2 = 0
for i in range(n):
    sum1 += arr[i][i]
for i in range(n):
    sum2 += arr[i][n-1-i]
dia = max(sum1, sum2)

res = max(row, col, dia)
print(res)

# 강의 코드
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
largest = -2147000000

# 행과 열의 계산은 동시에 진행
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j]  # 하나의 행에 존재하는 원소들의 합
        sum2 += a[j][i]  # 하나의 열에 존재하는 원소들의 합
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

# 두 대각선 중 최댓값
sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-1-i]
if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2

print(largest)