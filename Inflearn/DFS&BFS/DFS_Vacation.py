# 휴가


# 내가 작성한 코드 - 정답
def DFS(T, P):
    global Max
    if T > n+1:
        return
    if T == n+1:
        if P > Max:
            Max = P
    else:
        if P > Max:
            Max = P
        for i in range(T, n+1):
            if ch[i] == 0:
                if i + arr[i][0] > n:  # 상담 후 날짜가 근무 날짜를 넘어가면 안된다
                    for j in range(i, n + 1):  # for문의 마지막 범위가 n을 넘어가면 안된다 - n이 최대 근무 날짜
                        ch[j] = 1
                else:
                    for j in range(i, i + arr[i][0]):
                        ch[j] = 1
                DFS(i + arr[i][0], P + arr[i][1])
                if i + arr[i][0] > n:
                    for j in range(i, n + 1):
                        ch[j] = 0
                else:
                    for j in range(i, i + arr[i][0]):
                        ch[j] = 0


if __name__=="__main__":
    n = int(input())
    arr = [(0, 0)]
    for _ in range(n):
        t, p = map(int, input().split())
        arr.append((t, p))
    ch = [0] * (n+1)
    Max = 0
    DFS(1, 0)
    print(Max)


# 강의 코드
def DFS(L, Sum):
    global res
    if L == n+1:
        if Sum > res:
            res = Sum
    else:
        if L + T[L] <= n+1:  # 상담을 마친 다음날이 여행 시작 날짜를 넘어가면 안됨
            DFS(L+T[L], Sum+P[L])  # L+T[L]: 상담을 마친 다음날
        DFS(L+1, Sum)  # 오늘 상담을 하지 않는 경우 다음날 상담을 한다.


if __name__=="__main__":
    n = int(input())
    T = list()  # 날짜
    P = list()  # 수익
    # 내 코드에선 튜플로 T와 P를 묶고 리스트에 추가함
    for i in range(n):
        a, b = map(int, input().split())
        T.append(a)
        P.append(b)
    res = -2147000000
    T.insert(0, 0)  # index를 날짜로 사용하기 위해서 맨 앞에 0을 insert해준다.
    P.insert(0, 0)  # index를 날짜로 사용하기 위해서 맨 앞에 0을 insert해준다.
    DFS(1, 0)
    print(res)