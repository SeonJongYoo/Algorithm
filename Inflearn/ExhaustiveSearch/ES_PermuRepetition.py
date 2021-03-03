# 중복순열 구하기(DFS)


# 내가 작성한 코드
# 부분집합 구하기의 활용 문제라고 생각함
# 중복이 허용되므로 함수를 호출할 때마다 전체 집합에서 원소를 선택하도록 해야한다.
# 즉, 처음에 1이 사용되는 경우와 사용되지 않는 경우로 나누고 그 다음에도 1에 대해서 연산을 진행한다.
def DFS(v, M):
    global cnt
    x = M
    if x < 1:
        for i in range(1, n+1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
        print(temp)
        temp.clear()
        cnt = 0
    else:
        while cnt < n:
            x -= 1
            temp.append(ch[v])
            DFS(v, x)
            x = m
            cnt += 1


if __name__ == "__main__":
    n, m = map(int, input().split())
    #ch = [0] * (n+1)
    ch = [i for i in range(n+1)]
    temp = []
    cnt = 0
    DFS(1, m)


# 강의 코드
# 상태트리 구성
# n의 크기만큼의 리스트를 선언
def DFS(L):  # L은 L번째 자리를 의미하면서 동시에 상태트리의 Level을 의미함
    global cnt
    if L == m:  # 종료지점 - L층이 m층이 됐을 때. 즉, L번째자리가 m-1번째 자리를 넘었을 때
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):  # 각 자리(상태트리의 Level)마다 올 수 있는 값은 항상 1, 2, 3, ..., n 중에 하나 - 중복해서 뽑을 수 있으므로
            res[L] = i  # res리스트에서 L번째 자리에 1이 오는 경우부터 n이 오는 경우까지 반복한다.
            DFS(L+1)  # L+1번째 자리의 경우를 나타냄


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m  # m번 중복하여 뽑은 숫자들을 한 줄에 표시한다.
    cnt = 0
    DFS(0)
    print(cnt)