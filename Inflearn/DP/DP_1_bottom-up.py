# 네트워크 선 자르기 Bottom-Up
# 내가 작성한 코드(강의 코드와 동일)

N = int(input())
dy = [1, 2]
for i in range(2, N):
    dy.append(dy[i-1] + dy[i-2])
print(dy[N-1])
