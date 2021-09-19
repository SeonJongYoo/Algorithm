# 스타트와 링크 - 비트마스크

# import sys
# import itertools as it
#
# def DFS(L, s):
#     global start, Min
#     if L == n//2:
#         tstart = []
#         link = []
#         for i in range(n):
#             tmp = 1 << i
#             if start & tmp != tmp:
#                 link.append(i)
#             else:
#                 tstart.append(i)
#         sability = 0
#         lability = 0
#         scom = it.combinations(tstart, 2)
#         lcom = it.combinations(link, 2)
#         for x in scom:
#             sability += S[x[0]][x[1]] + S[x[1]][x[0]]
#         for x in lcom:
#             lability += S[x[0]][x[1]] + S[x[1]][x[0]]
#         Min = min(abs(sability-lability), Min)
#         if Min == 0:
#             print(0)
#             sys.exit(0)
#     else:
#         for i in range(s, n):
#             start |= 1 << i
#             DFS(L + 1, i + 1)
#             start &= ~(1 << i)
#
#
# n = int(sys.stdin.readline().rstrip())
# S = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
# start = 1
# Min = 100000
# DFS(1, 1)
# print(Min)


# 다른 풀이 - 비트 마스크 - 시간초과
# import sys
#
#
# n = int(sys.stdin.readline().rstrip())
# S = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
# Min = 100000
# for i in range(1 << n):
#     start = []
#     link = []
#     # 팀 구분하기
#     for j in range(n):
#         if i & (1 << j) == 0:
#             start.append(j)
#         else:
#             link.append(j)
#     if len(start) > n//2 or len(link) > n//2:
#         continue
#     ab_start = 0
#     ab_link = 0
#     for x in range(n//2):
#         for y in range(n//2):
#             if x == y:
#                 continue
#             ab_start += S[start[x]][start[y]]
#             ab_link += S[link[x]][link[y]]
#     Min = min(abs(ab_start-ab_link), Min)
#     if Min == 0:
#         print(Min)
#         sys.exit(0)
# print(Min)
#print(Min)