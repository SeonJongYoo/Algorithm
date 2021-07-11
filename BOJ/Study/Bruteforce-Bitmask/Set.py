# 집합


import sys

n = int(sys.stdin.readline().rstrip())
S = 0
num = 20
all_S = 0
while num > 0:
    tmp = 1 << num
    all_S |= tmp
    num -= 1
for _ in range(n):
    command = list(map(str, sys.stdin.readline().rstrip().split()))
    if command[0] == "add":
        tmp = 1 << int(command[1])
        S |= tmp
    elif command[0] == "remove":
        tmp = 1 << int(command[1])
        S &= ~tmp
    elif command[0] == "check":
        tmp = 1 << int(command[1])
        tmp_S = S
        tmp_S &= tmp
        if tmp_S == tmp:
            print(1)
        else:
            print(0)
    elif command[0] == "toggle":
        tmp = 1 << int(command[1])
        tmp_S = S
        tmp_S &= tmp
        if tmp_S == tmp:
            S &= ~tmp
        else:
            S |= tmp
    elif command[0] == "all":
        S |= all_S
    elif command[0] == "empty":
        S &= 0