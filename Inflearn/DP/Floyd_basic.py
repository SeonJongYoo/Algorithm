# 플로이드 워샬 알고리즘 - 그래프 최단거리

# 강의 코드
n, m = map(int, input().split())
dis = [[5000] *(n+1) for _ in range(n+1)]
for i in range(1, n+1): 
    dis[i][i] = 0 # 자기 자신에서 자기 자신까지의 비용은 0
for i in range(m):
    a, b, c = map(int, input().split())
    dis[a][b] = c # a에서 b까지 직접 이동하는데 드는 최소 비용은 c
# k: i에서 j까지의 경로중 거쳐가는 노드, k가 증가하면서 dis리스트는 계속 갱신됨
# *******************중요**************************
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
# ************************************************
# 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if dis[i][j] == 5000:
            print("M", end=' ')
        else:
            print(dis[i][j], end=' ')
    print()