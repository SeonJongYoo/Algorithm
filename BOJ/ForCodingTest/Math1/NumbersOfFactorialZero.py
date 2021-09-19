# 팩토리얼 0의 개수

# 내가 작성한 코드
# 모두 계산 후 끝자리 0의 존재를 파악함 -> 비효율적
# import sys
#
#
# def Fac(num):
#     if num == 0:
#         return 1
#     if num == 1:
#         return 1
#     return num * Fac(num-1)
#
#
# n = int(sys.stdin.readline().rstrip())
# res = Fac(n)
# cnt = 0
# while True:
#     div = res % 10
#     res //= 10
#     if div == 0:
#         cnt += 1
#     else:
#         break
# print(cnt)


# 내가 작성한 코드 - 정답 코드
# 팩토리얼을 직접 계산할 필요가 없다!!
# 0이 존재한다는 것은 2와 5 한 쌍이 몇 개 존재하는지를 파악하면 된다.
# 2x5 1개 - 0이 1개, 2x5 2개 - 0이 2개...
# 단 4와 25와 같은 2와 5의 제곱수는 1번씩 더 계산해야한다.
import sys
n = int(sys.stdin.readline().rstrip())
cnt = 0
n2 = 0
n5 = 0
if n != 0:
    while n != 1:
        k = 2
        tmp = n
        if tmp%2 == 0 or tmp%5 == 0:
            while tmp != 1:
                if tmp % k == 0:
                    tmp /= k
                    if k == 2:
                        n2 += 1
                    elif k == 5:
                        n5 += 1
                else:
                    k += 1
        n -= 1
    cnt = min(n2, n5)
print(cnt)