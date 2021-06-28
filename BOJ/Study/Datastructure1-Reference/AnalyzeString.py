# 문자열 분석
import sys

while True:
    s = sys.stdin.readline().rstrip('\n')
    if not s:
        break
    c1, c2, c3, c4 = 0, 0, 0, 0
    for x in s:
        if 64 < ord(x) < 91:
            c1 += 1
        elif 96 < ord(x) < 123:
            c2 += 1
        elif 47 < ord(x) < 58:
            c3 += 1
        else:
            c4 += 1
    print(c2, c1, c3, c4)
