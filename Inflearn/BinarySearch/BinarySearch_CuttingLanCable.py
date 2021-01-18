# 랜선자르기 - 결정 알고리즘
# 이분검색 사용
# lt, rt, mid를 정해주기 위한 범위를 생각하는 것이 핵심!

# 내가 작성한 코드
# 이분 검색 사용 X
# timeout error 발생 - 원인: 주어진 리스트의 최솟값에서 1씩 감소하며 정답을 찾아감
k, n = map(int, input().split())
arr = []
for i in range(k):
    a = int(input())
    arr.append(a)
arr.sort()
minimum = arr[0]
cnt = 0
while True:
    for i in range(k):
        list_num = arr[i]
        while list_num >= minimum:
            list_num -= minimum
            cnt += 1
    #print(cnt)
    if cnt == n:
        break
    else:
        minimum -= 1  # 1씩 감소시키기 때문에 연산량 증가!
        cnt = 0
print(minimum)

# 수정 코드
# 랜선의 길이는 주어진 리스트의 최댓값을 넘어가지 않는다.
# 1 ~ 최댓값 범위에서 이분검색을 적용!
# 나눗셈 연산의 몫이 어떤 역할을 하는지 생각하기!
# wrong answer or timeout error가 또 발생함.
k, n = map(int, input().split())
arr = []
for i in range(k):
    a = int(input())
    arr.append(a)
arr.sort()
lt, rt = 1, arr[k-1]
mid = (lt + rt) // 2
cnt = 0
while True:
    for i in range(k):
        number = arr[i]
        cnt += number // mid
    if cnt == n:  # 최댓값이 아닌 경우를 답으로 하는 경우 발생!
        break
    elif cnt > n:
        lt = mid + 1
        mid = (lt + rt) // 2
        cnt = 0
    else:
        rt = mid - 1
        mid = (lt + rt) // 2
        cnt = 0
print(mid)


# 강의 코드
def Count(len):  # 현재 mid값이 답이 될 수 있는지 판단하는 함수.
    cnt = 0
    for x in Line:
        cnt += (x // len)
    return cnt


k, n = map(int, input().split())
Line = []
res, largest = 0, 0
for i in range(k):
    tmp = int(input())
    Line.append(tmp)
    largest = max(largest, tmp)
lt = 1
rt = largest
while lt <= rt:  # Count(mid)의 결과가 나와도 최댓값을 찾을 때까지 반복하게됨
    mid = (lt + rt) // 2
    if Count(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)