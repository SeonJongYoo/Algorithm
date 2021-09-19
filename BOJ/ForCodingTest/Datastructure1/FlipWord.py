# 단어 뒤집기

import sys
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    words = sys.stdin.readline().rstrip().split()
    for word in words:
        stack = []
        for w in word:
            stack.append(w)
        while stack:
            print(stack.pop(), end="")
        print(end=" ")
    print()