# knapsack 알고리즘 - 동전 교환

# 내가 작성한 코드
# 동전이 무한개로 존재 -> 자원이 무한개 존재하는 경우
# 가방 문제와 동일한 알고리즘
n = int(input())
arr = list(map(int, input().split())) # 동전의 종류를 저장하는 리스트
m = int(input())
dy = [0] * (m+1) # dy 리스트의 index는 금액을 의미하고 원소는 해당 금액일 때 동전의 최소 개수를 의미한다.

for i in range(n):
    for j in range(arr[i], m+1):
        if dy[j] == 0:
            dy[j] = dy[j - arr[i]] + 1
        else:
            dy[j] = min(dy[j], dy[j - arr[i]] + 1)

print(dy[m])

# 강의 코드
n = int(input())
coin = list(map(int, input().split()))
m = int(input())
dy = [1000] * (m+1) # dy 리스트의 index는 금액을 의미하고 원소는 해당 금액일 때 동전의 최소 개수를 의미한다.
dy[0] = 0 # 0원을 거슬러 줄 때는 동전의 최소 개수는 0개
for i in range(n):
    for j in range(coin[i], m+1):
        dy[j] = min(dy[j], dy[j - coin[i]] + 1)

print(dy[m])