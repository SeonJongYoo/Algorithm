N = int(input())
temp = N; x = 0; y = 0

while 5*x + 3*y < temp:
    if N % 5 == 0:
        x += 1
        N = N - 5
    elif N % 3 == 0:
        y += 1
        N = N - 3
    else:
        if N >= 5:
            N = N - 5
            x += 1
        elif N >= 3:
            N = N - 3
            y += 1
        else:
            print(-1)
            break
    if N == 0:
        print(x + y)
