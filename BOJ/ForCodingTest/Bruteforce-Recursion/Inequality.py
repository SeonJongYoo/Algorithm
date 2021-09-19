# 부등호


# import time
# start = time.time()
# import sys
#
#
# def DFS(L):
#     global Max, Min, rMax, rMin
#     if L == k + 1:
#         print(seq)
#         for i in range(k):
#             if sign[i] == '<':
#                 if seq[i] > seq[i + 1]:
#                     return
#             elif sign[i] == '>':
#                 if seq[i] < seq[i + 1]:
#                     return
#         res = ""
#         for i in seq:
#             res += str(i)
#         print(res)
#         if int(res) > Max:
#             Max = int(res)
#             rMax = res
#         if int(res) < Min:
#             Min = int(res)
#             rMin = res
#     else:
#         for i in range(10):
#             if visit[i] == 0:
#                 visit[i] = 1
#                 seq.append(i)
#                 DFS(L + 1)
#                 seq.pop()
#                 visit[i] = 0
#
#
# k = int(sys.stdin.readline().rstrip())
# sign = list(map(str, sys.stdin.readline().rstrip().split()))
# visit = [0] * 10
# seq = []
# Max = 0
# Min = 9900000000
# rMax = ""
# rMin = ""
# DFS(0)
# print(rMax)
# print(rMin)
# end = time.time() - start
#print("time: ", end)

# pypy3 통과 / python3 시간초과
# import time
# start = time.time()
# import sys
#
#
# def MAX_DFS(L):
#     global Max
#     if Max != "":
#         return
#     if L == k + 1:
#         for i in range(k):
#             if sign[i] == '<':
#                 if seq1[i] > seq1[i + 1]:
#                     return
#             elif sign[i] == '>':
#                 if seq1[i] < seq1[i + 1]:
#                     return
#         res = ""
#         for i in seq1:
#             res += str(i)
#         Max = res
#         print(res)
#     else:
#         for i in range(9, -1, -1):
#             if visit1[i] == 0:
#                 visit1[i] = 1
#                 seq1.append(i)
#                 MAX_DFS(L + 1)
#                 seq1.pop()
#                 visit1[i] = 0
#
#
# def MIN_DFS(L):
#     if L == k + 1:
#         for i in range(k):
#             if sign[i] == '<':
#                 if seq2[i] > seq2[i + 1]:
#                     return
#             elif sign[i] == '>':
#                 if seq2[i] < seq2[i + 1]:
#                     return
#         res = ""
#         for i in seq2:
#             res += str(i)
#         print(res)
#         sys.exit(0)
#     else:
#         for i in range(10):
#             if visit2[i] == 0:
#                 visit2[i] = 1
#                 seq2.append(i)
#                 MIN_DFS(L + 1)
#                 seq2.pop()
#                 visit2[i] = 0
#
#
# k = int(sys.stdin.readline().rstrip())
# sign = list(map(str, sys.stdin.readline().rstrip().split()))
# visit1 = [0] * 10
# visit2 = [0] * 10
# seq1 = []
# seq2 = []
# Max = ""
# MAX_DFS(0)
# MIN_DFS(0)
# end = time.time() - start
# print("time: ", end)