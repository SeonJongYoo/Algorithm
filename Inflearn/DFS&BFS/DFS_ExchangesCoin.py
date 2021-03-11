# 동전 바꿔주기(DFS)


# 내가 작성한 코드
def DFS(L, Sum):
    global cnt
    if Sum > t:
        return
    if L == k:
        if Sum == t:
            cnt += 1
    else:
        for j in range(1, n[L]+1):
            DFS(L+1, Sum + p[L]*j)  # 동전을 쓰는 경우
        DFS(L+1, Sum)  # 동전을 쓰지 않는 경우


if __name__ == "__main__":
    t = int(input())
    k = int(input())
    p = list()
    n = list()
    for i in range(k):
        a, b = map(int, input().split())
        p.append(a)
        n.append(b)
    cnt = 0
    DFS(0, 0)
    print(cnt)

# 강의 코드 - 내 코드와 유사함
# 강의 코드는 동전을 사용하지 않는 경우도 리스트에 추가하여 연산을 수행함
# 내 코드에서는 동전을 사용하지 않는 경우엔 Sum에 값을 더하지 않고 재귀함수를 호출하도록함
# 상태트리 구성
# D(L)에 대해 edge는 각각 L번째 동전을 0개 사용하는 경우, 1개 사용하는 경우, 2개 사용하는 경우,
# ..., b개 사용하는 경우(b는 각 동전의 개수)
# Level을 진행하면서 동전의 합(Sum)을 동시에 계산한다. - Sum이 주어진 값을 넘어가면 cut edge!!
def DFS(L, Sum):  # L은 level이면서 각 동전에 접근하기 위한 index
    global cnt
    if Sum > T:  # cut edge
        return
    if L == k:
        if Sum == T:
            cnt += 1
    else:
        for i in range(cn[L]+1):
            DFS(L+1, Sum + (cv[L] * i))  # i는 사용할 동전의 개수를 의미하게됨
            # i = 0부터 시작하여 입력으로 주어진 동전의 개수까지의 값을 갖게됨

if __name__ == "__main__":
    T = int(input())
    k = int(input())
    cv = list()
    cn = list()
    for i in range(k):
        a, b = map(int, input().split())
        cv.append(a)
        cn.append(b)
    cnt = 0
    DFS(0, 0)