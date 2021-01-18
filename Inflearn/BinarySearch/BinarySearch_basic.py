# 이분 검색

# 내가 작성한 코드
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()  # 입력 받은 리스트를 오름차순으로 정렬
lt, rt = 0, n-1  # arr 리스트의 0번 째 index와 마지막 index
mid = (lt + rt) // 2  # 리스트의 중간값을 가리키는 index

while arr[mid] != m:
    if arr[mid] > m:
        rt = mid - 1
    elif arr[mid] < m:
        lt = mid + 1
    mid = (lt + rt) // 2
print(mid+1)  # 찾는 값의 위치 번호를 구해야하므로 index에 1을 더한다.

# 강의 코드
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
lt, rt = 0, n-1
while lt <= rt:
    mid = (lt + rt) // 2
    if a[mid] == m:
        print(mid+1)
        break
    elif a[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1