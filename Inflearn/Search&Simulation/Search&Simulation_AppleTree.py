# 사과나무(다이아몬드)

# 내가 작성한 코드
n = int(input())
grating = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for i in range(n//2 + 1):
    for j in range(n):
        if (n // 2) - i <= j <= (n // 2) + i:
            cnt += grating[i][j]
            if i != n // 2:
                cnt += grating[n - 1 - i][j]
print(cnt)

# 강의 코드
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
res = 0
s = e = n // 2
# 다이아몬드 형태
for i in range(n):
    for j in range(s, e+1):  # 범위 설정이 중요
        res += a[i][j]
    if i < n // 2:  # 중간 행 이전인 경우. 중간 행에 가까워질수록 i의 범위가 증가함
        s -= 1
        e += 1
    else:  # 중간 행 이후인 경우. 중간 행에서 멀어질수록 i의 범위가 감소함
        s += 1
        e -= 1
print(res)
