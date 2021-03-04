# **********조합 구하기*************
# *********************************

# 많은 문제에 응용됨!!!!!!!

# 조합은 순서를 생각하지 않는다
# 1 -> 2와 2 -> 1은 같은 경우!!


# 내가 작성한 코드 - 오답
'''def DFS(L):
    if L == m:
        for j in range(m):
            print(res[j], end=' ')
        print()
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                DFS(L+1)
                ch[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    ch = [0] * (n+1)
    DFS(0)'''


# 강의 코드
# 상태트리 구성하기
def DFS(L, s):
    global cnt
    if L == m:
        for j in range(m):
            print(res[j], end=' ')
        cnt += 1
        print()
    else:
        for i in range(s, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = i
                DFS(L+1, i+1)
                # for문의 시작이 계속 증가하도록하여 아예 이전에 뽑았던 숫자에 접근도 하지 않게함
                # D(1, 2), D(1, 3), D(1, 4), D(1, 5), ...
                # 첫번째 자리(i)가 1이면 두번째 자리는 1보다 큰 모든 숫자만 올 수 있음
                # 첫번째 자리(i)가 2이면 두번째 자리는 2보다 큰 모든 숫자만 올 수 있음...
                # 첫번째 자리(i)가 4이면 두번째 자리는 4보다 큰 숫자가 와야하지만 조건상 올 수 있는 숫자가 없음
                ch[i] = 0

if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    ch = [0] * (n + 1)
    cnt = 0
    DFS(0, 1)  # s = 1은 상태트리에서 가지를 뻗는 첫번째 숫자 - 뽑을 수 있는 숫자는 1 ~ n
    print(cnt)
    # D(1, 2) - 뽑을 수 있는 숫자는 2 ~ n, D(2, 3) - 뽑을 수 있는 숫자는 3 ~ n, ...

