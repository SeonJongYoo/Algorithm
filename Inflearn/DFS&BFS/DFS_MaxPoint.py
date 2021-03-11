# 최대 점수 구하기


# 조합 문제와 같은 유형
# time limit 에러가 계속 발생함 - 추가적인 cut edge가 필요
# *************m시간 안에 최대로 얻을 수 있는 점수*****************
# -> 딱 m시간에 끝나는게 아니라 문제를 푸는 모든 경우 중에서 최대 점수를 얻는 경우를 생각한다.
def DFS(T, p, s):
    global point
    if T > m:
        #print("HERE")
        return
    #if L == m:  # m시간 안에라는 조건을 생각해야 한다. - m시간을 딱 맞춰야 할 필요가 없다는 의미
        #print("p: ", p)
    else:
        if p > point:
            point = p
            #print("POINT: ", point)
        for i in range(s, n):
            if ch[i] == 0:
                ch[i] = 1
                #print("i, T, p: ", i, T, p)
                DFS(T + arr[i][0], p + arr[i][1], i+1)
                ch[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        a, b = map(int, input().split())
        x = (b, a)
        arr.append(x)
    point = 0
    ch = [0] * n
    DFS(0, 0, 0)
    print(point)


# 강의 코드
# 각 문제들을 전체 집합으로 생각하고 부분집합을 구한다.
# 부분집합에 속한 문제들은 푼 문제들이다.
def DFS(L, Sum, time):
    global res
    if L == n:  # 문제를 n번까지 다 푼 경우 - 종료 지점
        if Sum > res:
            res = Sum
    if time > m: # 문제를 푸는 시간이 제한시간 m을 넘어가는 경우
        return
    else:
        # 부분집합 구하기 문제와 같은 유형
        DFS(L+1, Sum + pv[L], time + pt[L])  # 문제를 푸는 경우
        DFS(L+1, Sum, time)  # 문제를 풀지 않는 경우


if __name__ == "__main__":
    n, m = map(int, input().split())
    pv = list()  # 문제 점수
    pt = list()  # 문제를 푸는 걸리는 시간
    for i in range(n):
        a, b = map(int, input().split())
        pv.append(a)  # 점수 리스트
        pt.append(b)  # 시간 리스트
    res = -2147000000
    DFS(0, 0, 0)
    print(res)
