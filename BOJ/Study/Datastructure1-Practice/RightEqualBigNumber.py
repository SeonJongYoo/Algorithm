# 오등큰수


# 내가 작성한 코드 - 성공
import sys
n = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
F = {}
for i in range(n):
    if A[i] not in F:
        F[A[i]] = 1
    else:
        F[A[i]] += 1
stack = [A.pop()]
res = [-1]
while A:
    tmp = A.pop()
    if F[tmp] >= F[stack[-1]]:
        for i in range(len(stack)-1, -1, -1):
            if F[tmp] < F[stack[i]]:
                res.append(stack[i])
                break
            else:
                stack.pop()
        if not stack:
            res.append(-1)
    else:
        res.append(stack[-1])
    stack.append(tmp)
for x in res[::-1]:
    print(x, end=" ")
