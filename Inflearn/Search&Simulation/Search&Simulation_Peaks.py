# 봉우리

# 내가 작성한 코드
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# 입력 받은 2차원 리스트의 첫 번째 행과 마지막 행에 모든 원소가 0인 리스트 삽입
arr.insert(0, [0]*n)
arr.append([0]*n)

# 입력 받은 2차원 리스트의 첫 번째 열과 마지막 열에 원소 0을 삽입
for i in arr:
    i.insert(0, 0)
    i.append(0)
# 위 과정으로 문제에서 주어진 격자판 완성

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        check = 0
        for k in range(4):  # 19 line ~ 23 line을 2줄로 작성 가능! - all() 함수: 인자가 참이면 True를 return
            if arr[i][j] > arr[i + dx[k]][j + dy[k]]:  # dx, dy 리스트를 이용하여 현재 좌표 기준 상하좌우 좌표와 크기를 비교
                check += 1
        if check == 4:
            cnt += 1
print(cnt)


# 강의 코드
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 어떤 좌표를 상하좌우 방향으로 이동시킬 수 있음

n = int(input())
a = [list[map(int, input().split())] for _ in range(n)]
a.insert(0, [0] * n)  # 이차원 리스트 a의 0번 행에 0으로 초기화된 리스트를 삽입
a.append([0] * n)  # 0으로 초기화된 리스트를 이차원 리스트 a의 마지막 행에 삽입
for x in a:  # 열의 맨 앞과 끝에 0을 추가
    x.insert(0, 0)
    x.append(0)

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        # all()은 괄호 내의 표현이 모두 참인 경우 true
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):  # 상하좌우보다 큰 값이 확인
            cnt += 1
print(cnt)