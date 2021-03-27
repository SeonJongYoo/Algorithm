# 중복순열 구하기
def DFS(L):
    global cnt
    if L == m+1:
        cnt += 1
        for i in range(1, m+1):
            print(ch[i], end=' ')
        print()
    else:
        for i in range(1, n+1):
            ch[L] = i
            DFS(L+1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    ch = [0]*(m+1)
    cnt = 0
    DFS(1)
    print(cnt)