# 나머지


# 모듈러 연산자의 분배법칙
a, b, c = map(int, input().split())
r1 = (a+b)%c
r2 = ((a%c) + (b%c))%c
r3 = (a*b)%c
r4 = ((a%c) * (b%c))%c
print(r1)
print(r2)
print(r3)
print(r4)