# 패션왕 신해빈


# 한 번에 여러 개의 옷을 입을 수 있다.
# 공식: (종류 당 의상의 개수+1) x (종류 당 의상의 개수 + 1) ... x (종류 당 의상의 개수 + 1) - 1
n = int(input())
if n == 0:
    print(0)
else:
    for _ in range(n):
        m = int(input())
        cloth = {}
        res = 0
        for _ in range(m):
            c1, c2 = map(str, input().split())
            if c2 not in cloth:
                cloth[c2] = 1
            else:
                cloth[c2] += 1
        tmp = 1
        for x in cloth.values():
            tmp *= (x+1)
        res = tmp-1
        print(res)