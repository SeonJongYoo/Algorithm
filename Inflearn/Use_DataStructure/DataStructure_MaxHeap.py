# 최대힙

# 루트 노드는 트리에서 가장 큰 값을 가짐

# 강의 코드
import heapq as hq  # heapq는 기본적으로 최소힙으로 동작함
# 최대힙으로 동작하기 위해 노드의 값에 -1을 곱하여 저장한다.
a = []  # heapq는 리스트가 필요 - heapq에 내장된 heappush와 heappop을 사용하면 리스트를 힙처럼 사용 가능!
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(-hq.heappop(a))  # a에서 루트 노드를 pop하여 return
    else:
        hq.heappush(a, -n)  # a리스트에 n을 push
