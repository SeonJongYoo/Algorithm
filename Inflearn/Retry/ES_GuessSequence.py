# 수열 추측하기
# 파스칼의 삼각형 - 이항계수!
# n = 3: 1 2 1
# n = 4: 1 3 3 1
# n = 5: 1 4 6 4 1
def DFS(L):
    if L == n+1:
        # 파스칼의 삼각형 전체를 계산해야 한다.
        tmp = []
        while L > 2:
            if L == n+1:
                for i in range(1, n):
                    tmp.append(res[i] + res[i + 1])
            else:
                for i in range(len(tmp)-1):
                    tmp[i] = tmp[i] + tmp[i+1]
                tmp.pop()
            L -= 1
        if tmp[0] == f:
            for i in range(1, n+1):
                print(res[i], end=' ')
            print()
            exit(0)
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                DFS(L+1)
                ch[i] = 0


if __name__ == "__main__":
    n, f = map(int, input().split())
    res = [0] * (n+1)
    ch = [0] * (n+1)
    DFS(1)


# 이항계수 이용
def DFS(L, Sum):
    if L == n+1:
        if Sum == f:
            for i in range(1, n+1):
                print(res[i], end=' ')
            print()
            exit(0)
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                DFS(L+1, Sum + b[L-1] * res[L])
                ch[i] = 0


if __name__ == "__main__":
    n, f = map(int, input().split())
    res = [0] * (n+1)
    ch = [0] * (n+1)
    b = [1]*n
    # 이항계수 초기화하기
    # n = 3: 1 2 1
    # n = 4: 1 3 3 1
    # n = 5: 1 4 6 4 1
    for i in range(1, n):
        b[i] = (b[i-1] * (n-i)) // i
    DFS(1, 0)