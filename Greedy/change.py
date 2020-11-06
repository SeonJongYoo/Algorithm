N = int(input())
N = 1000 - N
changes = [0 for _ in range(6)]

while N != 0:
    if N >= 500:
        N = N - 500
        changes[0] += 1
    elif N >= 100:
        N = N - 100
        changes[1] += 1
    elif N >= 50:
        N = N - 50
        changes[2] += 1
    elif N >= 10:
        N = N - 10
        changes[3] += 1
    elif N >= 5:
        N = N - 5
        changes[4] += 1
    else:
        N = N - 1
        changes[5] += 1

sum = 0
for i in range(6):
    sum += changes[i]

print(sum)
