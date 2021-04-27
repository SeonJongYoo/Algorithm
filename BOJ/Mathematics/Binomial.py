# 이항계수
# 내 풀이 - 모듈러 연산의 **분배법칙**은 곱셈, 덧셈, 뺄셈에 대해서만 적용된다! 나눗셈에 대해서 적용되지 않는다.
# 즉, nCk = n! / (n-k)!*k!을 p로 나눌 때 분모에 모듈러 연산이 적용되지 않는다.
# 수학 개념 오류
'''import sys
n, k = map(int, sys.stdin.readline().split(" "))
r = k
if k > n - k:
    r = n-k
ja = 1
mo = 1
res = 1
div = 1000000007
for i in range(r):
    ja *= n
    ja %= div
    mo *= r-i
    mo %= div
    n -= 1
    res = ja // mo
print(res)'''


# 이항계수 - 페르마의 소정리
# nCk = n! / (n-k)!*k!에 %p을 적용할 때 페르마의 소정리에 의해
# n! % p * (k!(n-k)!)**p-2 % p로 변형할 수 있다.
# -> 1 / (n-k)!*k!에 p에 대한 역원을 적용한 것!
# 팩토리얼 연산은 이분 탐색으로 구한다.
import sys


def power(N, R):
    if R == 0:
        return 1
    if R%2:  # R이 홀수
        return (power(N, R//2)**2 * N) % div
    else:  # R이 짝수
        return (power(N, R//2)**2) % div


if __name__ == "__main__":
    n, k = map(int, sys.stdin.readline().split())
    r = k
    if k > n - k:
        r = n-k
    div = 1000000007

    # n! 구하기
    factorial = [1 for _ in range(n+1)]
    for i in range(2, n+1):
        factorial[i] = factorial[i-1] * i % div

    # nCk 계산
    N_factorial = factorial[n]  # 분자
    Nk_factorial = (factorial[n-r]*factorial[r]) % div  # 분모

    # 페르마의 소정리
    # (A/B)%p
    # = A * B^-1 % p  ... B^-1은 p에 대한 B의 역원 -> a^(p-1) = a * a^(p-2) = 1(mod p)
    # = A * B^-1 * B^(p-1) % p
    # = A * B^(p-2) % p
    # = (A%p) * (B^(p-2) % p) % p
    res = (N_factorial % div) * (power(Nk_factorial, div-2) % div) % div
    print(res)



