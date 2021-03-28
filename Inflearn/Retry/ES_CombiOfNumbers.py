# 수들의 조합

def DFS(L, s):
    global cnt
    if L == k+1:
        Sum = 0
        for i in range(1, n+1):
            if ch[i] != 0:
                Sum += ch[i]
        if Sum % m == 0:
            cnt += 1
    else:
        for i in range(s, n+1):
            if ch[i] == 0:
                ch[i] = arr[i]
                DFS(L+1, i+1)
                ch[i] = 0


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.insert(0, 0)
    m = int(input())
    ch = [0]*(n+1)
    cnt = 0
    DFS(1, 1)
    print(cnt)