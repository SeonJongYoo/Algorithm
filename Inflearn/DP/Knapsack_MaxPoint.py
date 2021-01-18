# Knapsack 알고리즘 - 최대점수 구하기

# 내가 작성한 코드
# 한 유형당 한 개만 풀 수 있다 -> 자원이 유한개 존재하는 경우
'''n, m = map(int, input().split())
dy = [0] * (m+1)
# dy 리스트의 index는 푸는데 걸리는 시간을 의미하고 원소는 문제를 풀었을 때의 최대 점수를 의미한다.
arr = []
for i in range(n):
    #p, t = map(int, input().split())
    arr.append(tuple(map(int, input().split())))
    for j in range(arr[i][1], m+1):
        if i == 0:
            dy[j] = max(dy[j], arr[i][0])
        elif j-arr[i][1] >= arr[i][1]: # 문제 하나를 풀고 남은 시간을 확인한다. 남은 시간 동안에 풀 수 있는 다른 문제가 존재하는지 파악한다.
            dy[j] = max(dy[j], arr[i][0] + )

    print(dy)
print(dy[m])'''

# 강의 코드 - dy를 이차원 리스트로 선언한 경우
# dy 리스트의 크기가 커질수록 메모리가 커지므로 시간 복잡도가 증가함!
n, m = map(int, input().split())
dy = [[0]*(m+1) for _ in range(n+1)]
# dy 리스트의 index는 푸는데 걸리는 시간을 의미하고 원소는 문제를 풀었을 때의 최대 점수를 의미한다.

for i in range(1, n+1):
    p, t = map(int, input().split())
    for j in range(m+1):
        dy[i][j] = dy[i-1][j] # 이전 문제를 풀고나서 얻은 최대 점수를 다음 문제에 복사
    for j in range(t, m+1): # 주어진 문제를 푸는데 걸리는 시간부터 주어진 시간이 가장 클 때까지
        dy[i][j] = max(dy[i][j], dy[i-1][j-t] + p) # 같은 문제를 또 풀 수 없기 때문에 이전 문제의 정보를 가져온다.
print(dy[n][m])


# 강의 코드 - dy를 일차원 리스트로 선언한 경우
# 메모리 낭비, 복잡한 코드 작성 방지
n, m = map(int, input().split())
dy = [0]*(m+1)

for i in range(n):
    ps, pt = map(int, input().split())
    for j in range(m, pt-1, -1):
        # 문제를 풀 때 주어진 시간이 가장 클 때부터 주어진 문제를 푸는데 걸리는 시간까지 얻을 수 있는 최대 점수를 계산한다.
        dy[j] = max(dy[j], dy[j-pt] + ps)
        # dy[j-pt] : j라는 시간이 주어졌을 때 어떤 문제를 풀고 나서(pt시간 동안) 남은 시간동안에 얻을 수 있는 최대 점수
        # ps는 어떤 문제를 pt시간동안 풀고난 후 얻는 점수
print(dy[m])