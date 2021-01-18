# 카드 역배치

# 내가 작성한 코드
num = 10
arr = [0]
for i in range(1, 21):
    arr.append(i)
while num > 0:
    n, m = map(int, input().split())
    k = 0
    ep = ((m - n) // 2) + 1  # m - n이 짝수인 경우 1을 더할 필요는 없음!
    for n in range(n, n + ep):
        tmp = arr[n]
        arr[n] = arr[m - k]
        arr[m - k] = tmp
        k += 1
    num -= 1

for i in range(1, 21):
    print(arr[i], end=' ')


# 강의 코드
a = list(range(21))  # 1 ~ 20까지의 숫자를 저장하는 list
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1) // 2):
        a[s+i], a[e-i] = a[e-i], a[s+i]  # 두 변수의 값을 교환하는 방법!!

a.pop(0)  # 리스트의 맨 앞 원소를 삭제
for x in a:
    print(x, end=' ')
