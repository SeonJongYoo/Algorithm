# 최대공약수와 최소공배수

a, b = map(int, input().split())
r1, r2 = 0, 0
div = min(a, b)
while True:
    if a%div == 0 and b%div == 0:
        r1 = a//div
        r2 = b//div
        break
    else:
        div -= 1
print(div)
print(div*r1*r2)