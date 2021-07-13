# ABCDE


# A - B - C - D - E 관계
# import sys
# sys.setrecursionlimit(10000)
#
#
# def DFS(L, s):
#     visit[s] = L
#     if L == 5:
#         print(1)
#         sys.exit(0)
#     else:
#         for i in range(n):  # 첫 번째 노드부터 모두 탐색한다. - 시간복잡도 증가
#             if friend[s][i] == 1 and visit[i] == 0:
#                 visit[i] = 1
#                 DFS(L + 1, i)
#                 visit[i] = 0
#
#
# n, m = map(int, sys.stdin.readline().rstrip().split())
# friend = [[0] * n for _ in range(n)]
# for _ in range(m):
#     a, b = map(int, sys.stdin.readline().rstrip().split())
#     friend[a][b] = 1
#     friend[b][a] = 1
# visit = [0] * n
# # 탐색 시작 정점 정하기
# # 0부터 n-1까지
# for k in range(n):
#     DFS(0, k)
# print(0)


import sys
sys.setrecursionlimit(10000)


def DFS(node, fr):
    visit[node] = fr
    if fr == 5:
        print(1)
        sys.exit(0)
    else:
        for x in friend[node]:
            if visit[x] == 0:
                DFS(x, fr+1)
    visit[node] = 0


n, m = map(int, sys.stdin.readline().rstrip().split())
friend = [[] * n for _ in range(n)]  # 그래프 초기화 방법
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    friend[a].append(b)
    friend[b].append(a)

# 탐색 시작 정점 정하기
# 0부터 n-1까지
visit = [0] * n
for i in range(n):
    DFS(i, 1)
    #print(visit)
print(0)
