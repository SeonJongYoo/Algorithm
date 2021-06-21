# 가르침
import sys
import itertools as it

n, k = map(int, sys.stdin.readline().rstrip().split())
word = []
for _ in range(n):
    word.append(sys.stdin.readline().rstrip())
if k < 5:
    print(0)
else:
    south = ['a', 'c', 'i', 'n', 't']
    WordToNum = []
    num = 1
    for x in south:
        num |= 1 << (ord(x) - 97)
    teach = set()
    for x in word:
        tmp = num
        for y in x[4:-4]:
            if y not in south:
                tmp |= 1 << (ord(y) - 97)
                teach.add(y)
        WordToNum.append(tmp)
    if k-5 >= len(teach):
        print(n)
    else:
        Max = 0
        extract = it.combinations(teach, k-5)
        for x in extract:
            cnt = 0
            for y in x:
                num |= 1 << (ord(y) - 97)  # 최종적으로 학생들이 배운 글자
            for y in WordToNum:
                t = num & y
                if t == y:
                    cnt += 1
            if cnt > Max:
                Max = cnt
            for y in x:
                num &= ~(1 << (ord(y) - 97))
        print(Max)