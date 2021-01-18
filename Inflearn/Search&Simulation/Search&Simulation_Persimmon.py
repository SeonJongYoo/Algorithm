# 곶감(모래시계)

# 내가 작성한 코드
n = int(input())
arr1 = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for _ in range(m):
    a, b, c = map(int, input().split())
    if b == 0:  # 왼쪽 회전
        tmp = []
        tmp += arr1[a-1][c:n]
        tmp += arr1[a-1][:c]
        arr1[a-1][:] = tmp

    else:  # 오른쪽 회전
        tmp = []
        tmp += arr1[a-1][:]
        tmp += arr1[a-1][:c+1]
        arr1[a-1][:] = tmp
    print(arr1)


# 강의 코드
# 사과나무(다이아몬드)와는 반대로 중간 행에 가까워질수록 범위가 줄어들고 멀어질수록 범위가 늘어난다.
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for i in range(m):
    h, t, k = map(int, input().split())
    if t == 0:  # 왼쪽 방향 회전 - 맨 앞 원소를 꺼내서 맨 뒤에 넣어야한다.
        for _ in range(k):  # k만큼 회전해야함.
            a[h-1].append(a[h-1].pop(0))
            # 2행의 맨 앞을 삭제하고 이때 2행의 모든 원소는 한 칸씩 앞으로 당겨짐.이것을 다시 append!
    else:  # 오른쪽 방향 회전 - 맨 뒤 원소를 꺼내서 맨 앞에 넣어야한다.
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())

# 모래 시계 형태 - 다이아몬드 형태와 반대
res = 0
s, e = 0, n-1  # 다이아몬드에서는 s, e 모두 n // 2에서 시작
for i in range(n):
    for j in range(s, e):
       res += a[i][j]
    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(res)