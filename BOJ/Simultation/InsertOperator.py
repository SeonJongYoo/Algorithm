# 연산자 끼워넣기


# 순열 직접 구현 - 라이브러리와 시간 복잡도에서 차이 발생
# def DFS(L):
#     global Max, Min
#     if L == n-1:
#         chOper = []
#         for i in range(n-1):
#            chOper.append(operator[ch[i]-1])
#         if chOper in ck:
#             return
#         ck.append(chOper)
#         tmp = a[0]
#         j = 1
#         flag = False
#         for i in range(n-1):
#             if chOper[i] == '+':
#                 tmp += a[j]
#             elif chOper[i] == '-':
#                 tmp -= a[j]
#             elif chOper[i] == 'x':
#                 tmp *= a[j]
#             else:
#                 if tmp < 0:
#                     flag = True
#                     tmp = -tmp
#                 tmp //= a[j]
#                 if flag:
#                     flag = False
#                     tmp = -tmp
#             j+=1
#         if tmp > Max:
#             Max = tmp
#         if tmp < Min:
#             Min = tmp
#         print("Max, Min: ", Max, Min)
#     else:
#         for i in range(n-1):
#             if ch[i] == 0:
#                 ch[i] = L+1
#                 DFS(L+1)
#                 ch[i] = 0
#
#
# n = int(input())
# a = list(map(int, input().split()))
# op = list(map(int, input().split()))
# operator = []
# ch = [0]*(n-1)
# ck = []
# Max = -1000000000
# Min = 1000000000
# cnt = 0
# for i in range(4):
#     if op[i] != 0:
#         if i == 0:
#             for j in range(op[i]):
#                 operator.append('+')
#         elif i == 1:
#             for j in range(op[i]):
#                 operator.append('-')
#         elif i == 2:
#             for j in range(op[i]):
#                 operator.append('x')
#         else:
#             for j in range(op[i]):
#                 operator.append('//')
#
# if n > 2:
#     DFS(0)
# else:
#     if operator[0] == '+':
#         Max = a[0] + a[1]
#         Min = a[0] + a[1]
#     elif operator[0] == '-':
#         Max = a[0] - a[1]
#         Min = a[0] - a[1]
#     elif operator[0] == 'x':
#         Max = a[0] * a[1]
#         Min = a[0] * a[1]
#     else:
#         Max = a[0] // a[1]
#         Min = a[0] // a[1]
# print(Max)
# print(Min)


# 라이브러리 사용
# itertools - permuntations(순열)과 combinations(조합) API 이용 가능
# 각 API로 생성된 숫자들은 tuple 형태로 생성된다.
import itertools as it

n = int(input())
a = list(map(int, input().split()))
op = list(map(int, input().split()))
operator = []
Max = -1000000000
Min = 1000000000
for i in range(4):
    if op[i] != 0:
        if i == 0:
            for j in range(op[i]):
                operator.append('+')
        elif i == 1:
            for j in range(op[i]):
                operator.append('-')
        elif i == 2:
            for j in range(op[i]):
                operator.append('x')
        else:
            for j in range(op[i]):
                operator.append('//')

# set()으로 중복을 제거 - operator 리스트에는 중복되는 연산자가 존재
# 따라서 이대로 순열 또는 조합 생성 시 중복되는 경우가 발생 -> 중복 제거 필요!(set함수 사용)
op1 = set(it.permutations(operator))
res = 0
for x in op1:
    print(x)
    tmp = a[0]
    for i in range(n-1):
        flag = False
        if x[i] == '+':
            tmp += a[i+1]
        elif x[i] == '-':
            tmp -= a[i+1]
        elif x[i] == 'x':
            tmp *= a[i+1]
        else:
            if tmp < 0:
                flag = True
                tmp = -tmp
            tmp //= a[i+1]
            if flag:
                tmp = -tmp
    Min = min(tmp, Min)
    Max = max(tmp, Max)

print(Max)
print(Min)