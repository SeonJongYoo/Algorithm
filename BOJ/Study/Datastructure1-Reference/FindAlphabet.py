# 알파벳 찾기

import sys
s = sys.stdin.readline().rstrip()
alpha = [-1]*26
for i in range(len(s)):
    if alpha[ord(s[i])-97] != -1:
        continue
    alpha[ord(s[i])-97] = i
for x in alpha:
    print(x, end=" ")