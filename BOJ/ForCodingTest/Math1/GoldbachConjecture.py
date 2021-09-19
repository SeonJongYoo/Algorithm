# 골드바흐의 추측


# 내가 작성한 코드
import sys

ck = [0] * 1000001
ck[1] = 1
for i in range(2, 1000000):
    for j in range(i * i, 1000001, i):
        if ck[j] == 0:
            ck[j] = 1
while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    r1, r2 = 0, 0
    for i in range(3, n):
        if ck[i] == 0 and ck[n-i] == 0:
            r1, r2 = i, n-i
            break
    if r1 == 0 or r2 == 0:
        print("Goldbach's conjecture is wrong.")
    else:
        print(n, "=", r1, "+", r2)