# 경로탐색(그래프 DFS)


# 내가 작성한 코드
'''n, m = map(int, input().split())
g = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    g[a][b] = 1

cnt = 0
for k in range():
    temp = [1]
    for i in range(1, n+1):
        for j in range(i, n+1):
            if g[i][j] == 1:
                #print(j, end=' ')
                temp.append(j)
                break
    print(temp)'''


# 내가 작성한 코드2 - 정답
# 결국엔 "스택"에 대한 이해가 중요하다!!!!!!!!!!!
def DFS(v):
    global cnt, prior
    if v == n:
        cnt += 1
    else:
        for i in range(2, n+1):
            if res[i] == 0 and g[v][i] == 1:
                prior += 1
                res[v] = prior  # 방문한 노드는 체크해준다.
                DFS(i)
                res[v] = 0
                # res 리스트는 전역을 선언됨. 따라서, 함수가 종료되면 체크한 것을 풀어주어야한다.
                # 함수가 종료되어 이전 상황으로 돌아오면 앞에서 방문한 노드는 아직 방문한 것이 아니므로 원래대로 돌려놓는다.


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [[0] * (n + 1) for _ in range(n + 1)]
    cnt = 0
    prior = 0
    for i in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1  # 인접행렬 선언 및 초기화
    res = [0] * (n+1)
    DFS(1)
    print(cnt)


# 강의 코드
# 상태트리 구성하기
# 한번 방문한 노드는 다시 방문하면 안된다! - 노드를 방문할 때마다 체크. 체크 리스트 선언하여 관리
# 내가 작성한 코드와 완전히 일치
def DFS(v):
    global cnt
    if v == n:
        cnt += 1
    else:
        for i in range(1, n+1):
            if g[v][i] == 1 and ch[i] == 0:  # 내가 작성한 코드와 일치!!!
                ch[i] = 1  # 방문한 노드 체크하기
                DFS(i)
                ch[i] = 0  # 원래대로 돌려놓기


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [[0] * (n + 1) for _ in range(n + 1)]  # 인접행렬
    ch = [0] * (n+1)
    for i in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1  # 인접행렬 선언 및 초기화
        # 현재 문제에서 그래프는 방향 그래프이다.
    cnt = 0
    ch[1] = 1
    DFS(1)
    print(cnt)


# 강의 코드 - 경로 직접 출력하기
def DFS(v):
    global cnt
    if v == n:
        cnt += 1
        for x in path:
            print(x, end=' ')
        print()
    else:
        for i in range(1, n+1):
            if g[v][i] == 1 and ch[i] == 0:  # 내가 작성한 코드와 일치!!!
                ch[i] = 1  # 방문한 노드 체크하기
                # ***************
                path.append(i)  # 방문한 노드를 path에 넣어주기
                # ***************
                DFS(i)
                # ***************
                path.pop()  # 함수가 종료되어 이전 상황으로 돌아오면 앞에서 방문했던 노드는 pop한다.
                # ***************
                ch[i] = 0  # 원래대로 돌려놓기


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [[0] * (n + 1) for _ in range(n + 1)]  # 인접행렬
    ch = [0] * (n+1)
    for i in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1  # 인접행렬 선언 및 초기화
        # 현재 문제에서 그래프는 방향 그래프이다.
    cnt = 0
    path = []  # 경로를 저장할 리스트
    path.append(1)
    ch[1] = 1
    DFS(1)
    print(cnt)