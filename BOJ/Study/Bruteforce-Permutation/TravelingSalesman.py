# 외판원 순회 2


# 재귀 - 시간 초과
# import sys
#
#
# def DFS(L):
#     global Min
#     if L == n:
#         cost = 0
#         for i in range(n-1):
#             if cost > Min or city[arr[i]][arr[i+1]] == 0:  # 현재 계산 중인 비용이 전에 구한 최소 비용보다 큰 경우 or 가야할 길이 없는 경우
#                 return
#             cost += city[arr[i]][arr[i+1]]
#         if city[arr[n-1]][arr[0]] == 0:  # 원 위치로 돌아오는 길이 없는 경우
#             return
#         cost += city[arr[n-1]][arr[0]]  # 원 위치로 돌아오는 비용
#         Min = min(Min, cost)
#     else:
#         for i in range(n):
#             if visit[i] == 0:
#                 visit[i] = 1
#                 arr.append(i)
#                 DFS(L+1)
#                 arr.pop()
#                 visit[i] = 0
#
#
# n = int(sys.stdin.readline().rstrip())
# city = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
# Min = 10000001
# visit = [0]*n
# arr = []
# DFS(0)
# print(Min)


# 라이브러리 - 시간 초과
# import sys
# import itertools as it
#
# n = int(sys.stdin.readline().rstrip())
# city = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
# Min = 10000001
# arr = [i for i in range(n)]
#
# perm = it.permutations(arr)
# for x in perm:
#     print(x)
#     cost = 0
#     for i in range(len(x)-1):
#         if cost > Min or city[x[i]][x[i+1]] == 0:
#             break
#         cost += city[x[i]][x[i+1]]
#     if city[x[-1]][x[0]] == 0:
#         continue
#     cost += city[x[-1]][x[0]]
#     Min = min(Min, cost)
# print(Min)

# 정답 코드
import sys


def DFS(L, cost):
    global Min
    if cost > Min:
        return
    if L == n:
        if city[arr[-1]][arr[0]] == 0:  # 원 위치로 돌아오는 길이 없는 경우
            cost += 10000001
        else:
            cost += city[arr[-1]][arr[0]]
        Min = min(Min, cost)
    else:
        for i in range(n):
            if visit[i] == 0:
                visit[i] = 1
                arr.append(i)
                curr = 0
                if len(arr) > 1:
                    if city[arr[-2]][arr[-1]] == 0:  # 가는 길이 없는 경우
                        curr = 10000001
                    else:
                        curr = city[arr[-2]][arr[-1]]
                DFS(L+1, cost + curr)
                arr.pop()
                visit[i] = 0


n = int(sys.stdin.readline().rstrip())
city = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
Min = 10000001
visit = [0]*n
arr = []
DFS(0, 0)
print(Min)

