# BFS 스페셜 저지


# import sys
# from collections import deque
#
#
# n = int(sys.stdin.readline().rstrip())
# tree = [[]*(n+1) for _ in range(n+1)]
# for _ in range(n-1):
#     v1, v2 = map(int, sys.stdin.readline().rstrip().split())
#     tree[v1].append(v2)
#     tree[v2].append(v1)
# answer = list(map(int, sys.stdin.readline().rstrip().split()))
# print(tree)
# visit = [0]*(n+1)
# Q = deque()
# Q.append(1)
# visit[1] = 1
# k = 0
# while Q:
#     tmp = Q.popleft()
#     #print(tmp, end=" ")
#     if tmp != answer[k]:
#         print(0)
#         sys.exit(0)
#     else:
#         k += 1
#     for x in tree[tmp]:  # 방문하지 않은 정점을 방문하는 순서를 결정
#         if visit[x] == 0:
#             visit[x] = 1
#             Q.append(x)
# print(1)


# 정답 코드
# 인접 리스트 정렬하기(특정 기준으로) - lambda 사용
import sys
from collections import deque


n = int(sys.stdin.readline().rstrip())
tree = [[]*(n+1) for _ in range(n+1)]
for _ in range(n-1):
    v1, v2 = map(int, sys.stdin.readline().rstrip().split())
    tree[v1].append(v2)
    tree[v2].append(v1)
answer = list(map(int, sys.stdin.readline().rstrip().split()))
# 입력 순서 배열 초기화
order = [0]*(n+1)
tmp = 1
for i in answer:
    order[i] = tmp
    tmp += 1
for i in range(1, n+1):
    tree[i] = sorted(tree[i], key=lambda x: order[x])
visit = [0]*(n+1)
Q = deque()
Q.append(1)
visit[1] = 1
k = 0
while Q:
    tmp = Q.popleft()
    if tmp != answer[k]:
        print(0)
        sys.exit(0)
    else:
        k += 1
    for x in tree[tmp]:
        if visit[x] == 0:
            visit[x] = 1
            Q.append(x)
print(1)