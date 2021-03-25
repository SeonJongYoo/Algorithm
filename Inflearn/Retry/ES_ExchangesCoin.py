# 동전 교환 - 완전탐색
def DFS(L, Sum):
    global Min
    if L > Min:
        return
    if Sum > m:
        return
    if Sum == m:
        if L < Min:
            Min = L
    else:
        for i in range(n):
            DFS(L+1, Sum + coin[i])


if __name__ == "__main__":
    n = int(input())
    coin = list(map(int, input().split()))
    coin.sort(reverse=True)  # 큰 금액부터 거슬러 주면 동전의 개수를 줄일 수 있다!
    m = int(input())
    Min = 2147000000
    DFS(0, 0)
    print(Min)

