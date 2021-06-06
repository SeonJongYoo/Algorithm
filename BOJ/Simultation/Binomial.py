# 이항 계수

n, k = map(int, input().split())
Mo = 1
for i in range(k):
    Mo *= n
    n -= 1
Ja = 1
for i in range(1, k+1):
    Ja *= i
res = Mo / Ja
print(int(res))