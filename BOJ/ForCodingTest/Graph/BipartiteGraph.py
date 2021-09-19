# 이분 그래프

# import sys
# import itertools as it
# #sys.setrecursionlimit(100000)
#
#
# # first에 속하는 정점들은 서로 인접하지 않는다.
# # second에 속하는 정점들은 서로 인접하지 않는다.
# def DFS(L):
#     global flag
#     if L == v+1:
#         second = []
#         if not first or len(first) == v:
#             return
#         for x in range(2, v+1):
#             if visit[x] != 1:
#                 second.append(x)
#         # print(first)
#         # print(second)
#         # print("--------------------")
#         if len(first) > 1:
#             fcombi = it.combinations(first, 2)
#             for x in fcombi:
#                 if graph[x[0]][x[1]] == 1:
#                     return
#         if len(second) > 1:
#             scombi = it.combinations(second, 2)
#             for x in scombi:
#                 if graph[x[0]][x[1]] == 1:
#                     return
#         flag = True
#     else:
#         if visit[L] == 0:
#             visit[L] = 1
#             first.append(L)
#             DFS(L+1)
#             first.pop()
#             visit[L] = 0
#         DFS(L+1)
#
#
# k = int(sys.stdin.readline().rstrip())
# for _ in range(k):
#     v, e = map(int, sys.stdin.readline().rstrip().split())
#     graph = [[0]*(v+1) for _ in range(v+1)]  # 메모리 초과 원인
#     visit = [0]*(v+1)
#     for _ in range(e):
#         v1, v2 = map(int, sys.stdin.readline().rstrip().split())
#         graph[v1][v2] = 1
#         graph[v2][v1] = 1
#     first = [1]
#     visit[1] = 1
#     flag = False
#     DFS(2)
#     if flag:
#         print("YES")
#     else:
#         print("NO")


# 이분 그래프
# 연결된 노드는 서로 다른 색으로 구분한다.
# 현재 노드의 탐색을 시작하면 그 노드와 연결된 모든 노드들을 재귀를 통해 탐색한다.
# 탐색을 진행하면서 각 노드의 색깔을 지정한다.(1 or -1)
import sys
sys.setrecursionlimit(1000000)


def DFS(node, group):
    visit[node] = group  # 현재 노드의 색깔을 1로 지정
    for x in graph[node]:  # 현재 노드와 연결된 노드들 탐색
        if visit[x] == 0:  # 연결된 노드를 아직 방문하지 않은 경우
            r = DFS(x, -group)  # 현재 노드와 다른 색깔 -1로 지정
            if not r:
                return False
        elif visit[x] == visit[node]:  # 연결된 노드를 이전에  방문했을 때, 현재노드와 같은 색깔인 경우
            return False
    return True


k = int(sys.stdin.readline().rstrip())
for _ in range(k):
    v, e = map(int, sys.stdin.readline().rstrip().split())
    #graph = [[0]*(v+1) for _ in range(v+1)]  # 메모리 초과 원인
    graph = [[] for _ in range(v+1)]  # 비어있는 2차원 리스트 생성
    visit = [0]*(v+1)  # 노드를 방문했는지 체크하는 용도. 0이면 방문하지 않은 경우
    #  현재 노드와 연결된 노드의 색깔을 구분.
    for _ in range(e):
        v1, v2 = map(int, sys.stdin.readline().rstrip().split())
        # 연결된 노드끼리 리스트로 저장
        # graph[1]: 1번 노드와 연결된 모든 노드를 리스트로 저장함
        graph[v1].append(v2)
        graph[v2].append(v1)
    res = True
    # 1번 노드부터 탐색 시작
    for i in range(1, v+1):
        if visit[i] == 0:
            if not DFS(i, 1):
                res = False
                break
    if res:
        print("YES")
    else:
        print("NO")
    # print("YES" if res else "NO")