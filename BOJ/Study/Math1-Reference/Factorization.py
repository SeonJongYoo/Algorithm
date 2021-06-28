# 소인수분해

import sys
n = int(sys.stdin.readline().rstrip())
k = 2
while n != 1:
    if n%k == 0:
        n //= k
        print(k)
    else:
        k += 1