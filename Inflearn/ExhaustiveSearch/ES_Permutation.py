# 순열 구하기


# 내가 작성한 코드 - 정답
def DFS(L):
    global cnt
    if L == m:  # 자릿수를 넘어가면 종료
        for i in range(m):
            print(res[i], end=' ')
        cnt += 1
        print()
    else:
        for i in range(1, n+1):
            if i not in res:  # 3부터는 res 리스트에 있는 숫자로 판별되므로 아래 코드가 실행되지 않음
                # res를 계속 갱신해줘야함
                res[L] = i
                DFS(L+1)
                res[L] = 0  # 함수가 종료되면 이전에 res리스트에 저장했던 값은 의미가 없으므로 0으로 초기화한다.


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m  # m번 뽑는다 - 자릿수가 m
    cnt = 0
    DFS(0)
    print(cnt)


# 강의 코드
# 중복순열과 같은 유형
# 중복을 허용하지 않는 조건 - ch리스트를 만들어서 구현한다
def DFS(L):
    global cnt
    if L == m:
        for j in range(L):
            print(res[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                DFS(L+1)
                ch[i] = 0  # 함수가 종료되면 ch리스트의 값을 원래대로 돌려놓는다.
                # ---> 함수가 종료된 것은 이전 상황으로 돌아온 것과 같은 의미로 ch리스트를 원래대로 돌려놓는다.
if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * n
    ch = [0] * (n+1)
    cnt = 0
    DFS(0)
    print(cnt)