# 연산자 끼워넣기
import sys
import itertools as it
n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
oper = list(map(int, sys.stdin.readline().rstrip().split()))
Max = -1000000000
Min = 1000000000
if n == 2:
    num = a[0]
    for i in range(4):
        if oper[i] == 1:
            if i == 0:
                num += a[1]
            elif i == 1:
                num -= a[1]
            elif i == 2:
                num *= a[1]
            elif i == 3:
                if num < 0:
                    tmp = -num
                    tmp //= a[1]
                    num = -tmp
                else:
                    num //= a[1]
    Max = num
    Min = num
else:
    op = []
    for i in range(4):
        for j in range(oper[i]):
            op.append(i)
    new_op = set(it.permutations(op))  # 동일한 연산자가 포함되어 있으므로 중복을 제거해야 한다.
    for x in new_op:
        num = a[0]
        for i in range(n-1):
            if x[i] == 0:
                num += a[i+1]
            elif x[i] == 1:
                num -= a[i+1]
            elif x[i] == 2:
                num *= a[i+1]
            else:
                if num < 0:
                    tmp = -num
                    tmp //= a[i+1]
                    num = -tmp
                else:
                    num //= a[i+1]
        if num > Max:
            Max = num
        if num < Min:
            Min = num
print(Max)
print(Min)