# 부분집합 구하기
def DFS(L):
    if L == n+1:
        for i in range(1, n+1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
    else:
        ch[L] = 1
        DFS(L+1)
        ch[L] = 0
        DFS(L+1)


if __name__ == "__main__":
    n = int(input())
    ch = [0] * (n+1)
    DFS(1)