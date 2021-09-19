# 2진수 8진수

# import sys
#
#
# def toOct(N):
#     i, num = 0, 0
#     while i < 3:
#         re = N % 10
#         N //= 10
#         num += re*pow(2, i)
#         i += 1
#     return num
#
#
# n = int(sys.stdin.readline().rstrip())
# res = []
# if n == 0:
#     print(0)
# else:
#     while n != 0:
#         remains = n%1000
#         n //= 1000
#         res.append(toOct(remains))
#     for k in range(len(res)-1, -1, -1):
#         print(res[k], end="")


import sys


n = sys.stdin.readline().rstrip()
res = ""
if len(n)%3 == 0:
    for i in range(0, len(n), 3):
        num1 = int(n[i]) * 4
        num2 = int(n[i+1]) * 2
        num3 = int(n[i+2])
        res += str(num1+num2+num3)
else:
    if len(n) % 3 == 2:
        res = str(int(n[0]) * 2 + int(n[1]))
        for i in range(2, len(n), 3):
            num1 = int(n[i]) * 4
            num2 = int(n[i + 1]) * 2
            num3 = int(n[i + 2])
            res += str(num1+num2+num3)
    elif len(n) % 3 == 1:
        res = n[0]
        for i in range(1, len(n), 3):
            num1 = int(n[i]) * 4
            num2 = int(n[i + 1]) * 2
            num3 = int(n[i + 2])
            res += str(num1+num2+num3)
print(res)