# 가장 긴 증가하는 부분 수열 4

import sys
n = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
A.insert(0, 0)
dp = [0]*(n+1)
dp[1] = 1
dp2 = [[0], [A[1]]]
for i in range(2, n+1):
    Max = 0  # i번째 숫자까지의 수열에서 최대 길이를 구하기 위한 용도
    tmp = []
    for j in range(1, i):
        if A[i] > A[j] and dp[j] > Max:
            tmp = []
            Max = dp[j]
            for t in dp2[j]:
                tmp.append(t)
    tmp.append(A[i])
    dp[i] = Max + 1
    if not tmp:
        dp2.append(dp2[i-1])
    else:
        dp2.append(tmp)
print(max(dp))
for i in range(1, n+1):
    if len(dp2[i]) == max(dp):
        for j in dp2[i]:
            print(j, end=" ")
        break