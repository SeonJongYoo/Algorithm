# ROT13

import sys
s = sys.stdin.readline().rstrip()
for x in s:
    if ord(x) < 65:
        print(x, end="")
        continue
    if 64 < ord(x) < 91:
        tmp = ord(x) - 65
        tmp += 13
        tmp %= 26
        print(chr(tmp + 65), end="")
    else:
        tmp = ord(x) - 97
        tmp += 13
        tmp %= 26
        print(chr(tmp + 97), end="")
