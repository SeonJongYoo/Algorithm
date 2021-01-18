# Knapsack - 가방 문제

# 강의 코드
# 보석이 무한개로 존재 -> 자원이 무한개로 존재하는 경우
n, m = map(int, input().split())
dy = [0] * (n+1) # dy리스트의 index는 보석의 무게를 의미하고 원소는 가방에 담을 수 있는 보석의 최대 가치를 의미한다.
for i in range(n):
    w, v = map(int, input().split()) # 보석을 하나씩 읽는다.
    for j in range(w, n+1): # 가방에 넣는 보석의 무게부터 시작하여 dy 리스트를 초기화한다.
        dy[j] = max(dy[j], dy[j-w] + v) # 기존의 가치와 보석을 새로 넣었을 때의 가치 중 최댓값을 선택

print(dy[m])