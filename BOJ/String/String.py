# 문자열

from collections import deque

def DFS(L):
    global res
    if len(qa) == len(qb):
        r = diff(qa, qb)
        if r < res:
            res = r
    else:
        qa.appendleft(qb[0])
        DFS(L+1)
        qa.popleft()
        qa.append(qb[len(qb)-1])
        DFS(L+1)
        qa.pop()


def diff(x, y):
    cnt = 0
    for i in range(len(x)):
        if x[i] != y[i]:
            cnt += 1
    return cnt


a, b = map(str, input().split())
qa = deque(a)
qb = deque(b)
res = 2147000000
if len(qa) == len(qb):
    res = diff(qa, qb)
else:
    DFS(0)
print(res)
