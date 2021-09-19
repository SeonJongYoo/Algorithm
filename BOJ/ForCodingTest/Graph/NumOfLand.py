# 섬의 개수


import sys
sys.setrecursionlimit(10000)

def DFS(x, y, group):
    if x < 0 or x >= h or y < 0 or y >= w:
        return
    else:
        if Map[x][y] == 1 and visit[x][y] == 0:
            visit[x][y] = group
            DFS(x-1, y, group)
            DFS(x, y+1, group)
            DFS(x+1, y, group)
            DFS(x, y-1, group)
            DFS(x-1, y-1, group)
            DFS(x-1, y+1, group)
            DFS(x+1, y-1, group)
            DFS(x+1, y+1, group)


while True:
    w, h = map(int, sys.stdin.readline().rstrip().split())
    if w == 0 and h == 0:
        break
    Map = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(h)]
    visit = [[0]*w for _ in range(h)]
    #print(Map)
    #print(visit)
    k = 1
    for i in range(h):
        for j in range(w):
            if Map[i][j] == 1 and visit[i][j] == 0:
                DFS(i, j, k)
                k += 1
    print(k-1)
    # for i in range(h):
    #     for j in range(w):
    #         print(visit[i][j], end=" ")
    #     print()