# 알파벳 개수
import sys
s = sys.stdin.readline().rstrip()
alpha = [0]*26
for x in s:
    alpha[ord(x) - 97] += 1
for x in alpha:
    print(x, end=" ")