# 마구간 정하기 - 결정 알고리즘

# 내가 작성한 코드
# 답이 될 수 있는 범위: 주어진 마구간의 좌표들을 기준으로 좌표가 가장 작을 때 ~ 가장 클 때
# lt: 좌표가 가장 작을 때, rt: 좌표가 가장 클 때
# 좌표 list의 index를 통해 알고리즘을 구현하려했음.
# mid값의 의미를 제대로 파악하지 못함.
'''n, c = map(int, input().split())
arr = []
for _ in range(n):
    x = int(input())
    arr.append(x)
arr.sort()
lt = 0  # 주어진 마구간 좌표 중 최솟값의 index
rt = n-1  # 주어진 마구간 좌표 중 최댓값의 index

while lt <= rt:
    mid = (lt + rt) // 2'''



# 강의 코드
# 답이 될 수 있는 범위 정하기
# 가장 가까운 두 말의 거리의 최솟값 = 1 = lt , 최댓값 = 좌표의 최댓값 = rt
# mid가 답이 될 수 있다면, 가장 가까운 두 말 사이의 최대 거리가 mid임을 의미한다!
# 따라서, 모든 말들은 거리가 mid보다 크거나 같아야한다.
def Count(len):
    cnt = 1
    ep = Line[0]  # 첫 번째 말을 배치하는 지점. 주어진 좌표 중 제일 첫 번째 좌표
    for i in range(1, n):
        if Line[i] - ep > len:  # 최대 거리보다 큰 좌표에는 말을 배치할 수 있음
            cnt += 1
            ep = Line[i]
    return cnt

n, c = map(int, input().split())
Line = []
for _ in range(n):
    tmp = int(input())
    Line.append(tmp)
Line.sort()
lt = 1  # 가장 가까운 두 말 사이의 거리의 최솟값
rt = Line[n-1]  # 가장 가까운 두 말 사이의 거리의 최댓값
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= c:
        res = mid
        lt = mid + 1  # 현재의 최대 거리가 답이 될 수 있다면 이 거리보다 작은 최대 거리도
        # 모두 답이 될 수 있다.
    else:  # 답이 될 수 없는 경우. 가장 가까운 말 사이의 거리가 너무 커서
        # 현재 최대 거리에서는 마구간에 모든 말을 넣지 못한다.
        rt = mid - 1
print(res)
