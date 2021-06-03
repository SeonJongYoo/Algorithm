# 분산처리

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    res = 1
    tmp = []
    while True:
        res *= a%10
        res %= 10
        if res in tmp:
            break
        tmp.append(res)
    answer = tmp[b%len(tmp) - 1]
    if answer == 0:
        print(10)
    else:
        print(answer)