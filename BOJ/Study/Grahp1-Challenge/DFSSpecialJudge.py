# DFS 스페셜 저지


# pypy3 통과
# import sys
#
#
# def DFS(node):
#     global k
#     visit[node] = 1
#     k += 1
#     while True:
#         if k < n and answer[k] in tree[node]:
#             DFS(answer[k])
#         else:
#             break
#
#
# n = int(sys.stdin.readline().rstrip())
# tree = [[]*(n+1) for _ in range(n+1)]
# for _ in range(n-1):
#     v1, v2 = map(int, sys.stdin.readline().rstrip().split())
#     tree[v1].append(v2)
#     tree[v2].append(v1)
# answer = list(map(int, sys.stdin.readline().rstrip().split()))
# visit = [0]*(n+1)
# k = 0
# flag = False
# DFS(1)
# if k == n:
#     print(1)
# else:
#     print(0)



# 정답 코드
# 인접 리스트 정렬하기
import sys


def DFS(node):
    global k
    visit[node] = 1
    if node != answer[k]:
        print(0)
        sys.exit(0)
    k += 1
    for x in tree[node]:
        if visit[x] == 0:
            DFS(x)


n = int(sys.stdin.readline().rstrip())
tree = [[]*(n+1) for _ in range(n+1)]
for _ in range(n-1):
    v1, v2 = map(int, sys.stdin.readline().rstrip().split())
    tree[v1].append(v2)
    tree[v2].append(v1)
answer = list(map(int, sys.stdin.readline().rstrip().split()))
tmp = 1
# 입력 순서
order = [0]*(n+1)
for i in answer:
    order[i] = tmp
    tmp += 1
# 방문 순서에 따라 출력되는 값의 순서가 달라짐!
# answer가 올바른 순서인지 확인하기 위해 주어진 입력 answer 리스트를 기준으로 tree의 원소들을 정렬한다.
# idx = 1
for i in range(1, n+1):
    tree[i] = sorted(tree[i], key=lambda x: order[x])
visit = [0]*(n+1)
k = 0
DFS(1)
print(1)