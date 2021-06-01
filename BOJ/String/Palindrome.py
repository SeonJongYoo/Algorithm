# 팰린드롬수
import sys
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    arr = []
    while n != 0:
        arr.append(n%10)
        n = n//10
    if arr == arr[::-1]:
        print("yes")
    else:
        print("no")