# 퇴사2
# dp
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    t, p = map(int, input().split())
    arr.append((t, p))
arr.insert(0, (0, 0))
arr.append((0, 0))
dy = [0] * (n + 2)  # dy 리스트: index날짜까지 번 돈의 최댓값을 저장
Max = 0
for i in range(1, n+2):
    Max = max(Max, dy[i]) # 번 돈의 최댓값을 구하기 위한 장치
    if i + arr[i][0] <= n+1:  # 상담을 마친 다음날이 퇴사하는 날이거나 이전인 경우
        dy[i + arr[i][0]] = max(Max + arr[i][1], dy[i + arr[i][0]])
        # 오늘 상담을 하는 경우(Max+arr[i][1]) - 현재까지 상담 비용의 최댓값 + 오늘 상담 비용
        # 오늘 상담을 하지 않는 경우(dy[i+arr[i][0]]) - 현재까지 상담 비용의 최댓값만 추가
    #print("dy: ", dy)
print(Max)




# dfs
'''def DFS(L, Sum):
    global Max
    if L == n+1:
        if Sum > Max:
            Max = Sum
    else:
        if L + arr[L][0] <= n+1:
            DFS(L + arr[L][0], Sum + arr[L][1])
        DFS(L+1, Sum)  # 상담을 하지 않으면 다음날로 넘어간다. + 돈도 받지 않으므로 Sum만 넘긴다.


if __name__ == "__main__":
    n = int(input())
    arr = []
    for _ in range(n):
        t, p = map(int, input().split())
        arr.append((t, p))
    arr.insert(0, (0, 0))
    ch = [0]*(n+1)
    Max = 0
    DFS(1, 0)
    print(Max)'''