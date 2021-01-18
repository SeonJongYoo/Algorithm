# 그리디 알고리즘 - 창고 정리

# 내가 작성한 코드 - 강의 코드와 알고리즘 동일
L = int(input())
arr = list(map(int, input().split()))
M = int(input())

while M > 0:
    arr.sort() # 매번 정렬한다.
    arr[L-1] -= 1 # 정렬하면 맨 처음과 맨 마지막은 항상 최솟값과 최댓값을 유지한다.
    arr[0] += 1
    M -= 1

arr.sort()
print(arr[L-1] - arr[0])

# 강의 코드
L = int(input())
a = list(map(int, input().split()))
m = int(input())

a.sort()
for _ in range(m):
    a[0] += 1
    a[L-1] -= 1
    a.sort() # 연산 후 최솟값과 최댓값이 변경될 수 있으므로 다시 한번 정렬한다.

print(a[L-1] - a[0])
