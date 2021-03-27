# 바둑이 승차 - DFS
# 추가적인 cut-edge가 필요함
def DFS(L, Sum, ck):
    global Max
    if Sum + (Total - ck) < Max:  # Total - ck: 앞으로 부분집합에 적용할지 말지 판단해야할 원소들의 합
        return
    if Sum > c:
        return
    if L == n:
        if Sum > Max:
            Max = Sum
    else:
        DFS(L+1, Sum + w[L], ck + w[L])
        DFS(L+1, Sum, ck + w[L])
        # ck: 현재 부분집합으로 적용할지 말지 판단한 원소들의 합


if __name__ == "__main__":
    c, n = map(int, input().split())
    w = []
    for _ in range(n):
        tmp = int(input())
        w.append(tmp)
    Max = 0
    Total = sum(w)
    DFS(0, 0, 0)
    print(Max)
