# 네트워크 선 자르기 - BottomUp

n = int(input())
dy = [0, 1, 2]
# dy[1] = 1 -> 길이가 1m인 선을 자를 수 있는 경우의 수
# dy[2] = 2 -> 길이가 2m인 선을 자를 수 있는 경우의 수
for i in range(3, n+1):
    dy.append(dy[i-1] + dy[i-2])
print(dy[n])