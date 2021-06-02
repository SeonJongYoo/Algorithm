# 세로 읽기
import sys
arr = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(5)]
l = 0
for i in range(len(arr)):
    if l < len(arr[i]):
        l = len(arr[i])
for i in range(l):
    for j in range(5):
        if i < len(arr[j]):
            print(arr[j][i], end="")

