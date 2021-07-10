# 암호 만들기


import sys


def DFS1(L, s, n):
    if L == n:
        DFS2(0, 0, l-n)
    else:
        for i in range(s, vl):
            arr.append(vowel[i])
            DFS1(L + 1, i + 1, n)
            arr.pop()


def DFS2(L, s, n):
    if L == n:
        tmp = []
        for t in arr:
            tmp.append(t)
        tmp.sort()
        sarr = "".join(tmp)
        res.append(sarr)
    else:
        for i in range(s, cl):
            arr.append(consonant[i])
            DFS2(L + 1, i + 1, n)
            arr.pop()


l, c = map(int, sys.stdin.readline().rstrip().split())
alpha = list(map(str, sys.stdin.readline().rstrip().split()))
vowel = []
consonant = []
for x in alpha:
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        vowel.append(x)
    else:
        consonant.append(x)
vowel.sort()
consonant.sort()
vl = len(vowel)
cl = c - vl
limit = 1  # 모음 개수
res = []
# 모음은 최소 1개, 자음은 최소 2개
while True:
    if l - limit < 2:
        break
    arr = []
    DFS1(0, 0, limit)
    limit += 1
res.sort()
for x in res:
    print(x)