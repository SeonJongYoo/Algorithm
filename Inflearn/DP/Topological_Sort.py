# 위상 정렬 - 그래프
# 작업의 선후관계를 유지하면서 전체 작업의 순서를 짜는 알고리즘

# 강의 코드
n, m = map(int, input().split())
graph = [[100]*(n+1) for _ in range(n+1)]  # 방향 그래프를 인접행렬로 표현
degree = [0] * (n+1)  # 각 노드들의 진입 차수를 저장
queue = []  # 진입 차수가 0인 노드를 저장할 Queue
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    degree[b] += 1
for i in range(1, n+1):
    if degree[i] == 0:  # 진입 차수가 0인 노드들은 Queue에 삽입
        queue.append(i)

while queue:
    now = queue[0]
    queue.pop(0)  # 작업을 마칠 때마다 그 노드와 연결된 노드의 진입 차수를 1씩 감소!
    print(now, end=' ')
    for i in range(1, n+1):
        if graph[now][i] == 1:  # 그래프에서 작업을 마친 노드와 연결된 노드 찾기
            degree[i] -= 1
            if degree[i] == 0:  # 진입 차수가 0이 되는 순간 Queue에 삽입!
                queue.append(i)

