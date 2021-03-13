# 알파코드


# 내가 작성한 코드
# 숫자를 하나만 택하는 경우 두개를 택하는 경우
def DFS(L, code):
    global num
    if L == len(n):
        print("----> CODE: ", code)
        #num = num[0]
    else:
        # L == 4일 때 L + 1로 인해 index error 발생
        for i in range(2):
            if L + i < len(n):
                if alpha[L:L+i+1] == [0 for _ in range(i+1)]:
                    print("i: ", i)
                    print("L: ", L)
                    print("code: ", code)
                    print("alpha: ", alpha)
                    if int(n[L:L+i+1]) < 27:
                        print("here")
                        alpha[L:L+i+1] = [1 for _ in range(i+1)]
                        DFS(L+1, code + chr(int(n[L:L+i+1]) + 64))
                        alpha[L:L+i+1] = [0 for _ in range(i+1)]
                if alpha[L:L+i+1] == [1, 0]:
                    if int(n[L+i]) < 27:
                        print("here2")
                        alpha[L+i] = 1
                        DFS(L+1, code + chr(int(n[L+i]) + 64))
                        alpha[L+i] = 0
            else:
                print("****CODE: ", code)
# 주어진 숫자 n을 어떻게 분할할지
# 동전 분할 문제와 같은 유형?

if __name__ == "__main__":
    n = str(input())
    alpha = [0] * len(n)
    cnt = 0
    num = ""
    ch = [0] * 2
    DFS(0, "")


# 내가 작성한 코드2
# 상태트리 구성하기
# D(L)에서 L은 입력으로 주어진 숫자에 각각 접근하는 index를 의미.
# edge는 1 ~ 26까지 각각의 경우로 나눈다.
# 숫자가 한자릿수인 경우와 두자릿수인 경우 L의 증가 범위가 달라진다.
# 한자릿수인 경우 L+1, 두자릿수인 경우 L+2
def DFS(L, P):
    # L은 입력으로 주어진 숫자에 각각 접근
    # P는 res리스트의 index에 접근
    global cnt
    if L == len(n):
        cnt += 1
        for i in range(P):
            if res[i] != 0:
                print(chr(res[i]+64), end='')
        print()
    else:
        # 주어진 숫자 n에서 0인 부분에 대한 처리
        for j in range(2):
            if L + j < len(n):
                for i in range(1, 27):
                    if int(n[L:L+j+1]) == i:
                        if i < 10:
                            res[P] = i
                            DFS(L+1, P+1)
                        elif i < 27:
                            res[P] = i
                            DFS(L+2, P+1)  # 두자릿수인 경우 index에 +2를 해주어야 한다!!!
                        res[P] = 0


if __name__ == "__main__":
    n = str(input())
    res = [0] * len(n)  # n에서 선택한 숫자를 넣는 리스트
    cnt = 0
    DFS(0, 0)
    print(cnt)


# 강의 코드
# 상태트리 구성하기
# D(L)에서 L은 입력으로 주어진 숫자에 각각 접근하는 index를 의미.
# edge는 1 ~ 26까지 각각의 경우로 나눈다.
# 숫자가 한자릿수인 경우와 두자릿수인 경우 L의 증가 범위가 달라진다.
# 한자릿수인 경우 L+1, 두자릿수인 경우 L+2
def DFS(L, P):
    global cnt
    if L == n:
        cnt += 1
        for j in range(P):
            print(res[j], end='')
        print()
    else:
        for i in range(1, 27):
            if code[L] == i:  # 한자릿수 확인
                res[P] = i
                DFS(L+1, P+1)
            elif i >= 10 and code[L] == i // 10 and code[L+1] == i % 10:  # 두자릿수 확인
                # code[L] == i // 10 -> 두자릿수에 십의 자리 숫자 확인
                # code[L+1] == i % 10 -> 두자릿수에 일의 자리 숫자 확인
                # L이 주어진 리스트의 범위를 넘어가는 경우(code 리스트에서 마지막 문자를 확인하는 경우)
                # --> index 에러가 발생할 수 있음.
                # code.insert(n, -1) (- code 리스트에 n번째 값으로 임의의 값 -1을 넣어줌)이 없다면
                # 현재 반복문이 26까지 돌기 때문에 입력값의 마지막 숫자가 2이하인 경우 index에러가 발생함
                res[P] = i
                DFS(L+2, P+1)  # 두자릿수가 같다면 code 리스트의 index에 +2를 해줘야 다음 탐색시 겹치지 않음


if __name__ == "__main__":
    code = list(map(int, input()))
    n = len(code)
    code.insert(n, -1)  # index에러 처리를 위한 것.
    res = [0] * (n+3)  # n에서 선택한 숫자를 넣는 리스트 - 중요!!
    cnt = 0
    DFS(0, 0)
    print(cnt)