# 다음 순열
# import sys
# sys.setrecursionlimit(100000)
#
#
# def DFS(L):
#     global flag
#     if L == n:
#         if flag:
#             for i in res:
#                 print(i, end=" ")
#             sys.exit(0)
#         for i in range(n):
#             if res[i] != inp[i]:
#                 flag = False
#                 break
#             else:
#                 flag = True
#     else:
#         for i in range(n):
#             if visit[i] == 0:
#                 visit[i] = 1
#                 res.append(inp[i])
#                 DFS(L+1)
#                 res.pop()
#                 visit[i] = 0
#
#
# n = int(sys.stdin.readline().rstrip())
# inp = list(map(int, sys.stdin.readline().rstrip().split()))
# res = []
# visit = [0]*(n+1)
# flag = False
# ck = False
# for k in range(1, n+1):
#     if k == inp[n-k]:
#         ck = True
#     else:
#         ck = False
#         break
# if ck:
#     print(-1)
# else:
#     DFS(0)



# import sys
# import itertools as it
#
#
# n = int(sys.stdin.readline().rstrip())
# inp = list(map(int, sys.stdin.readline().rstrip().split()))
# ck = False
# for i in range(1, n+1):
#     if i == inp[n-i]:
#         ck = True
#     else:
#         ck = False
#         break
# if ck:
#     print(-1)
# else:
#     flag = False
#     seq = [i for i in range(1, n+1)]
#     perm = it.permutations(seq)
#     for x in perm:
#         print(x)
#         if flag:
#             for y in x:
#                 print(y, end=" ")
#             sys.exit(0)
#         for j in range(n):
#             if inp[j] == x[j]:
#                 flag = True
#             else:
#                 flag = False
#                 break


# 규칙성 찾기
# 1 2 3 4 -> 1 2 3 | 4
# 1 2 4 3 -> 1 2 | 4 3 -> 1 3 | 4 2 -> 1 3 2 4
# 1 3 2 4 -> 1 3 2 | 4 -> 1 3 4 2
import sys
n = int(sys.stdin.readline().rstrip())
inp = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(n-1, -1, -1):
    if i == 0:
        print(-1)
    elif i > 0 and inp[i] > inp[i-1]:
        idx = 0
        for j in range(i, n):
            if inp[i-1] < inp[j]:
                idx = j
        tmp = inp[idx]
        inp[idx] = inp[i-1]
        inp[i-1] = tmp
        arr1 = inp[:i]
        arr2 = inp[i:]
        arr2.sort()
        res = arr1 + arr2
        for x in res:
            print(x, end=" ")
        break

