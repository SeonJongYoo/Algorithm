# 조합 구하기


def DFS(L, s):
    global cnt
    if L == m+1:
        cnt += 1
        for i in range(1, n+1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
    else:
        for i in range(s, n+1):  # s는 이전에 선택한 숫자를 또 선택하지 못하게 하는 장치
            if ch[i] == 0:
                ch[i] = 1
                DFS(L+1, i+1)
                ch[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    ch = [0]*(n+1)  # 선택한 숫자를 기록하기 위한 장치
    cnt = 0
    DFS(1, 1)
    print(cnt)