# 회장 뽑기 - 플로이드 와샬
# 그래프 최단거리 문제와 같은 알고리즘

# 내가 작성한 코드
n = int(input())
dis = [[5000]*(n+1) for _ in range(n+1)]

for i in range(1, n+1): # 자기 자신은 친구가 아니므로 0(== 자신과 자신까지의 거리)
    dis[i][i] = 0

while True:
    x, y = map(int, input().split())
    if x == -1 and y == -1:
        break
    else:
        dis[x][y] = 1
        dis[y][x] = 1
    # x와 y가 친구 사이인 경우

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

arr = []
for i in range(1, n+1):
    max = -1
    for j in range(1, n+1):
        if dis[i][j] > max:
            max = dis[i][j]
    arr.append(max)

# 한 친구가 갖는 점수중 최댓값이 해당 점수가 된다.
boss_cnt = min(arr)
cnt = 0
for i in range(n):
    if arr[i] == boss_cnt:
        cnt += 1
print(boss_cnt, cnt)

for i in range(n):
    if arr[i] == boss_cnt:
        print(i+1, end=' ')
        
# 강의 코드 - 내가 작성한 코드와 동일한 알고리즘