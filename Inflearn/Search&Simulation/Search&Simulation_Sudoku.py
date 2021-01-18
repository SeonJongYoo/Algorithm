# 스도쿠 검사


# 내가 작성한 코드
def Check(List):  # 입력으로 받은 행, 열, 3x3 격자판이 1~9로 이루어져있는지 확인
    List.sort()
    for i in range(len(List)):
        if i+1 != List[i]:
            return False
    return True


arr = [list(map(int, input().split())) for _ in range(9)]

for i in range(len(arr)):  # 각 행을 확인
    check_row = []
    for j in range(len(arr)):
        check_row.append(arr[i][j])
    row = Check(check_row)
    if row is False:
        print("NO")
        exit(0)  # No이면 프로그램 종료

for i in range(len(arr)):  # 각 열을 확인
    check_column = []
    for j in range(len(arr)):
        check_column.append(arr[j][i])
    col = Check(check_column)
    if col is False:
        print("NO")
        exit(0)

# 어떤 좌표에 대해 상하좌우 및 양쪽 대각 좌표에 접근
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
for i in range(1, len(arr)-1, 3):  # 3x3 격자판 확인
    for j in range(1, len(arr)-1, 3):
        check_grid = [arr[i][j]]
        for k in range(8):
            check_grid.append(arr[i+dx[k]][j+dy[k]])
        grid = Check(check_grid)
        if grid is False:
            print("NO")
            exit(0)
print("YES")


# 강의 코드
def check(a):
    for i in range(9):
        ch1 = [0] * 10  # 행을 탐색하는 check list
        ch2 = [0] * 10  # 열을 탐색하는 check list
        for j in range(9):  # arr[i][j]에 해당하는 원소를 index로 하여 1을 저장
            ch1[a[i][j]] = 1  # 행을 check
            ch2[a[j][i]] = 1  # 열을 check
        if sum(ch1) != 9 or sum(ch2) != 9: # 숫자가 중복되어 나오는 경우 같은 곳에 1이 두번 저장됨
            # 합이 9가 될 수 없음!
            return False

    # 4중 for문
    # 총 9개의 그룹을 검사
    for i in range(3):  # 행을 0, 3, 6 3칸씩 검사
        for j in range(3):  # 열을 0, 3, 6 3칸씩 검사
            ch3 = [0] * 10  # 3x3 격자판을 탐색하는 check list
            # 그룹 내에서 9칸을 검사
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]] = 1  # 3x3 격자판 9개를 모두 탐색
            if sum(ch3) != 9:
                return False
    return True


a = [list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")