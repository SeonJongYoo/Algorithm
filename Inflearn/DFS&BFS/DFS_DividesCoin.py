# 동전 분배하기


# 내가 작성한 코드
# time error가 발생함 - 이미 구했던 값을 나중에 또 다시 계산하는 경우 발생
def DFS(L):
    global Min
    if L == n:
        if max(ch2) - min(ch2) >= Min or 0 in ch2:
            return
        for j in range(3):
            res.add(ch2[j])
        if len(res) != 3:
            res.clear()
            return
        if max(res) - min(res) < Min:
            Min = max(res) - min(res)
        res.clear()
    else:
        for j in range(3):
            if ch[L] == 0:
                ch[L] = 1
                ch2[j] += p[L]
                DFS(L+1)
                ch2[j] -= p[L]
                ch[L] = 0


if __name__ == "__main__":
    n = int(input())
    p = list()
    for i in range(n):
        x = int(input())
        p.append(x)
    Min = 2147000000
    ch = [0] * n
    ch2 = [0] * 3
    res = set()
    DFS(0)
    print(Min)


# 내가 작성한 코드2
# DFS 문제는 상태트리 구성하기 - 가장 중요!!!!!!!!!!!!
# D(L)에서 edge는 각각 L번째 동전을 문제에 A에게 주는 경우, B에게 주는 경우, C에게 주는 경우로 나눈다.
# 내가 작성한 코드1에 비해 코드가 간단해졌지만 time error는 여전히 발생함
# 이미 구했던 값을 나중에 또 다시 계산하는 경우 발생 - 문제오류
def DFS(L):  # L은 각각 입력으로 주어진 동전의 index를 의미한다.
    global Min
    if L == n:  # people이 구성되었을 때 서로 같은 값이 있는 확인해야한다. - 세 사람의 총액이 서로 달라야 하므로!
        #print(people)
        for i in range(3):
            res.add(people[i])
        if len(res) < 3:
            res.clear()
            return
        if max(res) - min(res) < Min:
            Min = max(res) - min(res)
        res.clear()
    else:
        for i in range(3):
            people[i] += cv[L]
            DFS(L+1)
            people[i] -= cv[L]


if __name__ == "__main__":
    n = int(input())
    cv = list()
    for i in range(n):
        x = int(input())
        cv.append(x)
    people = [0] * 3
    Min = 2147000000
    res = set()
    DFS(0)
    print(Min)


# 강의 코드
# DFS문제는 상태트리 구성하기 - 가장 중요!!!!!!!!!!!!
# D(L)에서 edge는 각각 L번째 동전을 문제에 A에게 주는 경우, B에게 주는 경우, C에게 주는 경우로 나눈다.
def DFS(L):  # L은 각각 입력으로 주어진 동전의 index를 의미한다.
    global res
    if L == n:
        cha = max(money) - min(money)
        if cha < res:
            tmp = set()  # 내가 작성한 코드와 같다!
            for x in money:
                tmp.add(x)
            if len(tmp) == 3:
                res = cha

    else:
        for i in range(3):
            money[i] += coin[L]
            DFS(L+1)
            money[i] -= coin[L]  # 이전 상황으로 돌아오기 때문에

if __name__ == "__main__":
    n = int(input())
    coin = list()
    money = [0] * 3  # A, B, C 각각의 총액
    res = 2147000000
    for i in range(n):
        coin.append(int(input()))
    DFS(0)
    print(res)