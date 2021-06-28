# 접미사 배열

import sys
s = sys.stdin.readline().rstrip()
suffix = []
for i in range(len(s)):
    suffix.append(s[i:])
suffix.sort()
for x in suffix:
    print(x)