# 진법 변환 2


import sys
n, b = map(int, sys.stdin.readline().rstrip().split())
res = ""
while n != 0:
    re = n%b
    n //= b
    if re >= 10:
        re += 55
        res += chr(re)
    else:
        res += str(re)
print(res[::-1])
