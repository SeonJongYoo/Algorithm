# BABBA

k = int(input())
dp1 = [0]*(k+1)
dp2 = [0]*(k+1)
dp1[0] = 1
dp2[1] = 1
for i in range(2, k+1):
    dp1[i] = dp2[i-1]
    dp2[i] = dp1[i-1] + dp2[i-1]
print(dp1[k], dp2[k])