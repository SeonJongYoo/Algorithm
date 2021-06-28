# 네 수
import sys
a, b, c, d = map(str, sys.stdin.readline().rstrip().split())
n1 = a+b
n2 = c+d
print(int(n1) + int(n2))