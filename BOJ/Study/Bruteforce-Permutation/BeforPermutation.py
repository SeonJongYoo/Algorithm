# 이전 순열

# import sys
# import itertools as it
#
#
# n = int(sys.stdin.readline().rstrip())
# inp = list(map(int, sys.stdin.readline().rstrip().split()))
# ck = False
# for i in range(1, n+1):
#     if i == inp[i-1]:
#         ck = True
#     else:
#         ck = False
#         break
# if ck:
#     print(-1)
# else:
#     flag = False
#     seq = [i for i in range(n, 0, -1)]
#     perm = it.permutations(seq)
#     for x in perm:
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
import sys
n = int(sys.stdin.readline().rstrip())
inp = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(n-1, -1, -1):
    if i == 0:
        print(-1)
    elif i > 0 and inp[i] < inp[i-1]:
        idx = 0
        for j in range(i, n):
            if inp[i-1] > inp[j]:
                idx = j
        tmp = inp[idx]
        inp[idx] = inp[i-1]
        inp[i-1] = tmp
        arr1 = inp[:i]
        arr2 = inp[i:]
        arr2.sort(reverse=True)
        res = arr1 + arr2
        for x in res:
            print(x, end=" ")
        break