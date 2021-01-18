# 네트워크 선 자르기 Top-Down
# 강의 코드
N = int(input())

dy = [0] * (N+1)
def DFS(n):
    if dy[n] > 0:
        return dy[n]
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        dy[n] = DFS(n-1) + DFS(n-2)
        return dy[n]

print(DFS(N))