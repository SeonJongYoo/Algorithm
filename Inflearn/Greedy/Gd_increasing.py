# 증가수열 만들기 - 그리디 알고리즘

# 내가 작성한 코드 - 리스트의 맨 처음과 끝 중에서 작은 값을 뽑고 이 값을 temp 변수에 저장한다.
# 이후 리스트의 맨 앞과 끝을 가리키는 index를 선언하고 반복문을 돌면서 temp와 리스트의 양 쪽 끝 값을 비교한다.
# temp는 수열의 마지막 항
N = int(input())
arr = list(map(int, input().split()))

string = ''
i, j = 0, N-1
temp = min(arr[i], arr[j])
if temp == arr[i]:
    string += 'L'
    i += 1
else:
    string += 'R'
    j -= 1
while i != j and temp <= arr[i] or temp <= arr[j]:
    if arr[i] <= arr[j]:
        if temp <= arr[i]:
            string += 'L'
            temp = arr[i]
            i += 1
        else:
            string += 'R'
            temp = arr[j]
            j -= 1
    else:
        if temp <= arr[j]:
            string += 'R'
            temp = arr[j]
            j -= 1
        else:
            string += 'L'
            temp = arr[i]
            i += 1
if i == j and temp < arr[i]:
    string += 'L'

print(len(string))
print(string)

# 강의 코드 - 리스트의 맨 앞과 마지막을 각각 문자와 함께 튜플 형태로 임시 리스트에 저장하고
# 그 중 작은 값을 수열의 마지막 항으로 설정!
# 연산을 할 때마다 수열의 마지막 항을 초기화 한다.
n = int(input())
a = list(map(int, input().split()))
lt = 0
rt = n-1
last = 0 # 수열의 마지막 항
res = ""
tmp = []

while lt <= rt:
    if a[lt] > last:
        tmp.append((a[lt], 'L')) # 튜플 형태로 리스트에 저장
    if a[rt] > last:
        tmp.append((a[rt], 'R'))
    tmp.sort() # 튜플의 첫 번째 원소를 기준으로 정렬
    if len(tmp) == 0: # 임시 리스트에 아무것도 들어가 있지 않은 상태 - 종료!
        break
    else:
        res = res + tmp[0][1] # 정렬한 임시 리스트에서 작은 숫자의 문자를 저장
        last = tmp[0][0] # 수열의 마지막 항을 기록
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    tmp.clear() # 리스트 내 모든 원소를 지운다. clear()함수도 기억하자.

print(len(res))
print(res)