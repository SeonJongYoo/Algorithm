# 이모티콘

# import sys
# from collections import deque
#
# s = int(sys.stdin.readline().rstrip())
# Q = deque()
# Q.append(1)
# time = 0
# clip = [[0]]
# while Q:
#     size = len(Q)
#     print(Q)
#     # print("-------------")
#     # print("time: ", time)
#     tmp = []
#     for i in range(size):
#         screen = Q.popleft()
#         if screen == s:
#             print(time)
#             sys.exit(0)
#         # 1번
#         tmp.append(screen)
#         Q.append(screen)
#         # 2번
#         if time > 0 and clip[time][i]:
#             tmp.append(clip[time][i])
#             Q.append(screen+clip[time][i])
#         # 3번
#         if screen > s:
#             tmp.append(clip[time][i])
#             Q.append(screen-1)
#     clip.append(tmp)
#     time += 1
#     print(clip)


import sys
from collections import deque

s = int(sys.stdin.readline().rstrip())
Q = deque()
Q.append((1, 0))
time = 0
while Q:
    size = len(Q)
    # print(Q)
    # print("time: ", time)
    # print("-------------")
    tmp = set()
    for _ in range(size):
        sc = Q.popleft()
        if sc[0] == s:
            print(time)
            sys.exit(0)
        # 1번
        tmp.add((sc[0], sc[0]))
        #Q.append((sc[0], sc[0]))
        # 2번
        if sc[1] != 0:
            tmp.add((sc[0]+sc[1], sc[1]))
            #Q.append((sc[0]+sc[1], sc[1]))
        # 3번
        if sc[0] > 0:
            tmp.add((sc[0]-1, sc[1]))
            #Q.append((sc[0]-1, sc[1]))
    Q = deque(tmp)
    time += 1