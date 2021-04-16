# 1로 만들기


# Top-Down - Recursion Error 발생
'''def DFS(x):
    if x == 1:
        return 0
    if dp[x] != 0:
        return dp[x]
    else:
        dp[x] = 1 + DFS(x - 1)
        if x%2 == 0:
            tmp = 1 + DFS(x//2)
            if dp[x] > tmp:
                dp[x] = tmp
        if x%3 == 0:
            tmp = 1 + DFS(x//3)
            if dp[x] > tmp:
                dp[x] = tmp

    return dp[x]


if __name__ == "__main__":
    x = int(input())
    dp = [0]*(x+1)
    res = DFS(x)
    for i in range(1, x+1):
        print(dp[i], end=' ')
    print()
    print(res)'''


# Bottom-Up
x = int(input())
dp = [0]*(x+1)
if x >= 3:
    dp[2] = 1
    dp[3] = 1
if x == 2:
    dp[2] = 1
MAX = 100000
for i in range(4, x+1):
    t1, t2, t3 = MAX, MAX, MAX
    if i%3 == 0:
        t1 = dp[i//3]
    if i%2 == 0:
        t2 = dp[i//2]
    t3 = dp[i-1]
    dp[i] = 1 + min(t1, t2, t3)
print(dp[x])