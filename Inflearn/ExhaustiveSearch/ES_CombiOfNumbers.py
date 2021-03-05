# 수들의 조합


# 내가 작성한 코드
# 조합 구하기 문제 응용
# 전역으로 선언된 ch리스트는 조합 문제에서 현재 사용했던 숫자를 1로 체크하여
# 다음번에 다시 사용하지 않기 위한 것이다.
# 하지만, DFS함수의 인자 s로 인해 ch리스트는 필요없다.
# s에 의해서 이전에 사용한 숫자에 대해 접근하지 않기 때문이다.
def DFS(L, s):
    global cnt
    if L == k:
        if sum(res) % m == 0:
            cnt += 1
    else:
        for i in range(s, n):
            res[L] = arr[i]
            DFS(L+1, i+1)


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    m = int(input())
    res = [0] * k
    cnt = 0
    DFS(0, 0)
    print(cnt)


# 강의 코드
# DFS의 매개변수를 3개로 잡는다.
# s는 for문의 시작index를 결정
# Sum은 숫자를 뽑을 때마다 합을 구하기 위한 용도
# 내 코드와 다른점은 뽑은 숫자들의 합을 DFS함수를 재귀함수로 호출할 때마다 동시에 합을 계산한다.
# 내 코드는 숫자를 다 뽑고 난 후에 합을 계산하기 때문에 for문을 한번 더 사용한다. - 시간복잡도 증가
# 또한, 이 문제는 뽑은 숫자들의 합만 구하면 되기때문에 굳이 뽑은 숫자들을 res리스트에 기록할 필요가 없다.
def DFS(L, s, Sum):
    global cnt
    if L == k:
        if Sum % m == 0:
            cnt += 1
    else:
        for i in range(s, n):
            DFS(L+1, i+1, Sum+a[i])


if __name__ == "__main__":
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    DFS(0, 0, 0)
    print(cnt)


# 강의 코드2
# 라이브러리를 이용한 조합 구하기
import itertools as it
n, k = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())
cnt = 0
for x in it.combinations(a, k): # a리스트에서 k개를 뽑는다.
    if sum(x) % m == 0:
        cnt += 1
print(cnt)
