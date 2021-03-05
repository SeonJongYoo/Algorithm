# 인접행렬(가중치 방향 그래프)


# 내가 작성한 코드
def DFS(v, s):
    temp = [0] * n
    if len(res) == n:
        for i in range(n):
            for j in range(n):
                print(res[i][j], end=' ')
            print()
        exit(0)
    else:
        for i in range(s, m):
            #print("v, i: ", v, i)
            #print("temp: ", temp)
            if v == info[i][0]:
                temp[info[i][1]-1] = info[i][2]
            else:
                #print("HERE")
                res.append(temp)
                #print("res: ", res)
                #print("------------------")
                DFS(v+1, i)


if __name__ == "__main__":
    n, m = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(m)]
    res = []
    DFS(1, 0)


# 강의 코드
# 재귀함수 사용X
# 2차원 리스트 선언(인접행렬) - 행과 열의 각 index는 노드를 의미한다.
# 초기에 2차원 리스트(인접행렬)의 모든 원소는 0으로 초기화
# a노드에서 b노드로 이동할 수 있다면 2차원 리스트의 원소를 1로 초기화
n, m = map(int, input().split())
g = [[0] * n for _ in range(n)] # 인접행렬 선언 및 초기화
for i in range(m):
    a, b, c = map(int, input().split())
    g[a][b] = c

for i in range(1, n+1):
    for j in range(1, n+1):
        print(g[i][j], end=' ')
    print()