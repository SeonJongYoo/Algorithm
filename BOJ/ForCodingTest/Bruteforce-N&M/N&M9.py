# N과 M 9

#시간 초과
import sys


def DFS(L):
    if L == m:
        ans.add(tuple(res))
    else:
        for i in range(n):
            if visit[i] == 0:
                visit[i] = 1
                res.append(arr[i])
                DFS(L + 1)
                visit[i] = 0
                res.pop()
            # if visit[i] == 0:
            #     visit[i] = 1
            #     res.append(arr[i])
            #     DFS(L+1, i+1)
            #     visit[i] = 0
            #     res.pop()


n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr.sort()
res = []
visit = [0]*n
ans = set()
DFS(0)
ans = list(ans)
ans.sort()
for x in ans:
    for y in x:
        print(y, end=" ")
    print()


# import sys
#
#
# def DFS(L):
#     if L == m:
#         print(res)
#     else:
#         for i in range(n):
#             if visit[i] == 0:
#                 visit[i] = 1
#                 res.append(arr[i])
#                 DFS(L + 1)
#                 visit[i] = 0
#                 res.pop()
#
#
# n, m = map(int, sys.stdin.readline().rstrip().split())
# arr = list(map(int, sys.stdin.readline().rstrip().split()))
# arr.sort()
# res = []
# visit = [0]*n
# DFS(0)