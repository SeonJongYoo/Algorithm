# 네트워크 선 자르기 - TopDown
n = int(input())
dy = [0] * (n + 1)


def DFS(L):
    if dy[L] > 0:  # 이전에 구했던 값이면 리스트에서 찾아 바로 return!
        return dy[L]
    if L == 1:  # 길이가 1m인 선을 자르는 경우
        return 1
    if L == 2:  # 길이가 2m인 선을 자르는 경우
        return 2
    else:
        dy[L] = DFS(L - 1) + DFS(L - 2)  # TopDown 기본 구조
        return dy[L]


DFS(n)
print(dy[n])
