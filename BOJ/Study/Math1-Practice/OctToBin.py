# 8진수 2진수

# 시간 초과
# import sys
#
#
# def toBin(N):
#     res = ""
#     while N != 0:
#         remain = N % 2
#         N //= 2
#         res += str(remain)
#     while len(res) != 3:
#         res += '0'
#     return res
#
#
# n = int(sys.stdin.readline().rstrip())
# ans = ""
# while n != 0:
#     remains = n%10
#     n //= 10
#     ans += toBin(remains)
# if ans[-1] == '0':
#     ans = ans[:-1]
# print(ans[::-1])


import sys


def toBin(N):
    res = ""
    while N != 0:
        remain = N % 2
        N //= 2
        res += str(remain)
    while len(res) != 3:
        res += '0'
    return res[::-1]


n = sys.stdin.readline().rstrip()
ans = ""
if n == '0':
    print(0)
else:
    for x in n:
        ans += toBin(int(x))
    idx = 0
    for i in range(len(ans)):
        if ans[i] == '1':
            idx = i
            break
    print(ans[idx:])