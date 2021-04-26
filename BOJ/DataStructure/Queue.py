# 큐
'''
import sys
n = int(sys.stdin.readline())
Q = []
front = 0
back = -1
stand = -1
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    if "push" in s:
        tmp = s.split(" ")
        Q.append(int(tmp[1]))
        back += 1
    elif s == "pop":
        if back == stand:
            print(-1)
        else:
            print(Q[front])
            Q[front] = 0
            front += 1
            stand += 1
    elif s == "size":
        if back == stand:
            print(0)
        else:
            print(back+1)
    elif s == "empty":
        if back == stand:
            print(1)
        else:
            print(0)
    elif s == "front":
        if back == stand:
            print(-1)
        else:
            print(Q[front])
    elif s == "back":
        if back == stand:
            print(-1)
        else:
            print(Q[back])'''


from collections import deque
import sys
n = int(sys.stdin.readline())
Q = deque()
front = 0
back = -1
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    if "push" in s:
        tmp = s.split(" ")
        Q.append(int(tmp[1]))
        back += 1
    elif s == "pop":
        if not Q:
            print(-1)
        else:
            dl = Q.popleft()
            back -= 1
            print(dl)
    elif s == "size":
        if not Q:
            print(0)
        else:
            print(len(Q))
    elif s == "empty":
        if not Q:
            print(1)
        else:
            print(0)
    elif s == "front":
        if not Q:
            print(-1)
        else:
            print(Q[front])
    elif s == "back":
        if not Q:
            print(-1)
        else:
            print(Q[back])
