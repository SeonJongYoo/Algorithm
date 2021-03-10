# 최소힙

# 강의 코드
import heapq as hq
a = []  # heapq는 리스트가 필요 - heapq에 내장된 heappush와 heappop을 사용하면 리스트를 힙처럼 사용 가능!
while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a))  # a에서 루트 노드를 pop하여 return
    else:
        hq.heappush(a, n)  # a리스트에 n을 push