# 격자판 회문수


# 내가 작성한 코드
def Check(num):  # 회문인지 판단하는 함수
    if num == num[::-1]:
        return True
    else:
        return False


arr = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for k in range(7):
    for i in range(3):  # 주어진 격자판에서 행만 검사하여 5자리 회문수인지 판단
        s1 = ""
        for j in range(5):
            s1 += str(arr[k][i+j])
        if Check(s1) is True:
            cnt += 1

    for i in range(3):  # 주어진 격자판에서 열만 검사하여 5자리 회문수인지 판단
        s2 = ""
        for j in range(5):
            s2 += str(arr[i+j][k])
        if Check(s2) is True:
            cnt += 1

print(cnt)


# 강의 코드
board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(3):
    for j in range(7):
        tmp = board[j][i:i+5]  # slice 기능 기억하기!
        if tmp == tmp[::-1]:  # 회문인지 판단
            cnt += 1
        for k in range(2):
            if board[i+k][j] != board[i+5-k-1][j]:  # 각 열의 5자리가 회문인지 판단
                break
        else:
            cnt += 1
        #  for if else문 - for문이 정상적으로 끝나면 else문 실행
        