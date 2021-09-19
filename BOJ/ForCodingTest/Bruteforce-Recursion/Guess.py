# 맞춰봐


# import sys
#
#
# def DFS(L, Sum):
#     global cnt, nextLine
#     if L == n:
#         print(first)
#         k = 1
#         while cnt > 0:
#             nextLine = first[k:]
#             DFS(0, cnt)
#             cnt -= 1
#             k += 1
#     else:
#         if line[L] == '-':
#             for j in range(-1, -11, -1):
#                 if Sum + j < 0:
#                     first.append(j)
#                     DFS(L+1, Sum + j)
#                     first.pop()
#         elif line[L] == '+':
#             for j in range(1, 11):
#                 if Sum + j > 0:
#                     first.append(j)
#                     DFS(L + 1, Sum + j)
#                     first.pop()
#         else:
#             for j in range(-10, 11):
#                 if Sum + j == 0:
#                     first.append(j)
#                     DFS(L + 1, Sum + j)
#                     first.pop()
#
#
# def check(L, N, Sum):
#     if L == N:
#
#     else:
#         if :
#             check(L+1, N, Sum + nextLine[L])
#
#
# n = int(sys.stdin.readline().rstrip())
# num = list(map(str, sys.stdin.readline().rstrip()))
# # -+0+ / -2 5 -3 1
# # +++ / 5 -3 1
# # -- / -3 1
# # + / 1
# cnt = n-1
# first = []
# line = []
# for i in range(cnt):
#     line.append(num[i])
# nextLine = []
# DFS(0, 0)


import sys


def DFS(L, Sum):
    if n <= L < len(sign):
        if sign[L] == '-':
            if first[L-n] > 0:
                return
        elif sign[L] == '+':
            if fir
        else:

    else:
        if sign[L] == '-':
            for j in range(-1, -11, -1):
                if Sum + j < 0:
                    first.append(j)
                    DFS(L+1, Sum + j)
                    first.pop()
        elif sign[L] == '+':
            for j in range(1, 11):
                if Sum + j > 0:
                    first.append(j)
                    DFS(L + 1, Sum + j)
                    first.pop()
        else:
            for j in range(-10, 11):
                if Sum + j == 0:
                    first.append(j)
                    DFS(L + 1, Sum + j)
                    first.pop()


n = int(sys.stdin.readline().rstrip())
sign = list(map(str, sys.stdin.readline().rstrip()))
# -+0+ / -2 5 -3 1
# +++ / 5 -3 1
# -- / -3 1
# + / 1
first = []
DFS(0, 0)