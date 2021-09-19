# 제곱수의 합


# 초기 시간초과 발생 - min() 함수 사용
# if문으로 대체 후 통과!
import time
start = time.time()
import sys
n = int(sys.stdin.readline().rstrip())
dp = [0]*(n+1)
dp[1] = 1
# dp[i]: i이하의 제곱수들의 합으로 i를 나타낼 때 최소 항의 개수
for i in range(2, n+1):
    k = int(i**0.5)
    for j in range(k, 0, -1):  # 최대 루트 i부터 1까지 반복
        if dp[i] == 0:
            dp[i] = dp[i - j * j] + 1
        elif dp[i] > dp[i - j * j] + 1:
            dp[i] = dp[i - j * j] + 1
print(dp[n])
end = time.time() - start
print("time is: ", end)


# 통과 - 역순 탐색: 루트 i부터 1까지
# 기존 풀이와의 차이점
# dp 리스트의 초기화 - 모든 숫자를 제곱수 1로 표현한다면 항의 개수가 n개가 된다.
# dp[i] 초기화 시 if문과 min() 함수 사용 여부 - if문 사용 시 더 빠르다.
# import time
# start = time.time()
# import sys
# n = int(sys.stdin.readline().rstrip())
# dp = [i for i in range(n+1)]
# # dp[i]: i이하의 제곱수들의 합으로 i를 나타낼 때 최소 항의 개수
# for i in range(2, n+1):
#     k = int(i**0.5)
#     for j in range(k, 0, -1):  # 최대 루트 i부터 1까지 반복
#         if dp[i] > dp[i - j * j] + 1:
#             dp[i] = dp[i - j * j] + 1
# print(dp[n])
# end = time.time() - start
# print("time is: ", end)


# 통과 - 정방향 탐색: 1부터 루트 i까지
# import time
# start = time.time()
# import sys
# n = int(sys.stdin.readline().rstrip())
# dp = [i for i in range(n+1)]
# # dp[i]: i이하의 제곱수들의 합으로 i를 나타낼 때 최소 항의 개수
# for i in range(2, n+1):
#     k = int(i**0.5)
#     for j in range(1, k+1):  # 최대 1부터 루트 i까지 반복
#         if dp[i] > dp[i - j * j] + 1:
#             dp[i] = dp[i - j * j] + 1
# print(dp[n])
# end = time.time() - start
# print("time is: ", end)


# 통과 - 정방향 탐색 -> but 가장 느림
# import time
# start = time.time()
# import sys
# n = int(sys.stdin.readline().rstrip())
# dp = [i for i in range(n + 1)]
# for i in range(1, n + 1):
#     j = 1
#     while j * j <= i:  # 최대 1부터 루트 i까지 반복
#         if dp[i] > dp[i - j * j] + 1:
#             dp[i] = dp[i - j * j] + 1
#         j += 1
# print(dp[n])
# end = time.time() - start
# print(end)