# 그리드 알고리즘 - 씨름 선수

# 내가 작성한 코드 - 이중 for문 사용으로 비효율적인 코드
N = int(input())
info = []
for _ in range(N):
    h, w = map(int, input().split())
    info.append((h, w))
info.sort() # 키 순으로 정렬
cnt = 0
for i in range(N):
    for j in range(N):
        if i == j:
            cnt += 1
            continue
        else:
            if j > i and info[i][1] < info[j][1]:
                cnt -= 1
                break
print(cnt)

# 강의 코드
n = int(input())
body = []
for i in range(n):
    a, b = map(int, input().split())
    body.append((a, b))
body.sort(reverse=True)
largest = 0
cnt = 0
for x, y in body:
    if y > largest: # 기존에 저장된 몸무게보다 현재 위치에서 몸무게가 더 크면 갱신! 이중 for문을 사용하는 방식보다 빠름
        largest = y
        cnt += 1
print(cnt)