# 수들의 합

# 내가 작성한 코드
# 마지막 예제에서 timeout error 발생. 답은 1로 출력됨
n, m = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
for i in range(n):
    num = 0
    for j in range(i, n):
        num += A[j]
        if num == m:
            cnt += 1
            break
        elif num > m:
            break

print(cnt)


# 강의 코드
n, m = map(int, input().split())
a = list(map(int, input().split()))
lt, rt = 0, 1  # 주어진 리스트의 포인터 변수
tot = a[0]  # lt가 가리키는 곳부터 rt 바로 앞이 가리키는 곳까지의 합
cnt = 0
while True:
    if tot < m:  # 연속 부분합이 m보다 작은 경우. rt를 증가시켜 tot값에 원소를 더 추가함.
        if rt < n:
            tot += a[rt]
            rt += 1
        else:  # rt가 n인 경우. 더 이상 증가할 수 없음
            break
    elif tot == m:  # 연속 부분합이 m과 같은 경우
        cnt += 1
        tot -= a[lt]  # 첫 번째 lt의 원소를 빼서 두 번째 원소가 lt가 되므로 순서를 바꾸게됨
        lt += 1
    else:
        tot -= a[lt]  # 연속 부분합이 m보다 큰 경우. 첫 번째 lt의 원소를 빼서 순서를 변경.
        lt += 1
print(cnt)
