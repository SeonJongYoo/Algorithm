# 숫자 카드2

# 내가 작성한 코드 - Hash table
'''n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

# 중복이 되는 Key에서 문제 발생
darr2 = dict()
for i in range(m):
    darr2[arr2[i]] = i
res = [0]*m
for i in range(n):
    if arr1[i] not in darr2:
        continue
    res[darr2[arr1[i]]] += 1
for x in res:
    print(x, end=" ")'''

# Hash Table 방식
import sys
n = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().rstrip().split()))

res = {}
# 상근이 가지고 있는 숫자 카드에 대해 hash table 생성
for x in arr1:
    if x not in res:
        res[x] = 1
    elif x in res:
        res[x] += 1
# 상근이가 몇 개 가지고 있는지 검사할 카드들을 앞서 생성한 hash table에서 key값을 통해 참조
for x in arr2:
    if x not in res:
        print(0, end=" ")
        continue
    print(res[x], end=" ")



# 이진 탐색 방식1 - 시간 초과
'''import sys


# 찾으려는 값의 시작 위치 return
def lower(target):
    s = 0
    e = n - 1
    while s < e:
        mid = (s + e) // 2
        if arr1[mid] >= target:
            e = mid
        else:
            s = mid + 1
    return e


# 찾으려는 값의 마지막 위치+1 return
def upper(target):
    s = 0
    e = n - 1
    while s < e:
        mid = (s + e) // 2
        if arr1[mid] > target:
            e = mid
        else:
            s = mid + 1
    return e

n = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().rstrip().split()))

arr1.sort()
for i in range(m):
    start = lower(arr2[i])
    end = upper(arr2[i])
    # end가 arr1의 index 범위를 벗어나는 경우
    # end == n-1 조건 하나만 있으면 범위
    if arr2[i] == arr1[n-1] and end == n-1:
        end+=1
    print(end-start, end=" ")'''
    
# 이진 탐색2 - 시간 초과
'''import sys


# 찾으려는 값의 시작 위치 return
def binary(target):
    res = 0
    s = 0
    e = n - 1
    while s <= e:
        mid = (s + e) // 2
        if arr1[mid] == target:
            res = arr1[s:e+1].count(target)
            break
        elif arr1[mid] > target:
            e = mid-1
        else:
            s = mid+1
    return res


n = int(sys.stdin.readline())
arr1 = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline())
arr2 = list(map(int, sys.stdin.readline().rstrip().split()))
arr1.sort()
for i in range(m):
    result = binary(arr2[i])
    print(result, end=" ")'''