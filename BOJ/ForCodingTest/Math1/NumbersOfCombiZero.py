# 조합 0의 개수


# 내가 작성한 코드
# 초기
# 나눗셈 연산 시 개수의 차이 계산이 잘못되었다.
# 0은 2와 5에 의해 만들어진다.
# 2000000000!에서 2와 5의 개수를 일일이 찾는 것은 비효율적!
import sys


def ZeroInFac(N):
    N2, N5 = 0, 0
    i, j = 2, 5
    # N!에서 소인수 2의 개수 구하기
    while i <= N:
        N2 += N // i
        i *= 2
    # N!에서 소인수 5의 개수 구하기
    while j <= n:
        N5 += N // j
        j *= 5
    return N2, N5


n, m = map(int, sys.stdin.readline().rstrip().split())
n2, n5 = ZeroInFac(n)
m2, m5 = ZeroInFac(m)
nm2, nm5 = ZeroInFac(n-m)

mo2 = m2 + nm2
mo5 = m5 + nm5

res2 = n2 - mo2
res5 = n5 - mo5
print(min(res2, res5))
