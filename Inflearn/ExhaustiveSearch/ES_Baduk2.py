# 바둑이 승차(DFS)


# 내가 작성한 코드
# 부분집합 구하기 활용 문제
# timeout 에러 발생 - 시간복잡도를 줄일 필요가 있음
# 불필요한 연산이 계속됨 - s값이 M보다 작은 경우가 계속 발생함.
def DFS(v, s):
    global M, c
    if s > c:  # C킬로그램(무게제한)을 넘는 경우는 바로 return해버린다.
        return
    if v == n:  # 종료지점
        if s > M:
            M = s
    else:
        DFS(v+1, s + arr[v])
        DFS(v+1, s)


if __name__ == "__main__":
    c, n = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    M = 0
    DFS(0, 0)
    print(M)


# 강의 코드
# 시간복잡도 개선을 위해 추가적인 cut이 필요함
def DFS(L, s, ts):
    global result, total
    if s + (total - ts) < result:  # ts: 부분집합에 적용할지말지 이미 판단한 원소들의 합
        # total - ts: 앞으로 판단해야할 원소들의 합
        # 즉, 현재까지 구한 s(부분집합으로 사용하기로한 원소들의 합)에 total-ts를 더했을 때
        # 지금까지 구한 최댓값(result)보다 작다면 굳이 연산을 진행할 필요가 없으므로 return!!
        return
    if s > c:  # s가 무게제한(c)을 넘으면 안됨
        return
    if L == n:  # 종료지점 - 부분집합이 완성되는 지점
        if s > result:
            result = s
    else:
        DFS(L+1, s + a[L], ts + a[L])  # a[L]을 부분집합의 원소로 참여시키는 경우
        DFS(L+1, s, ts + a[L])  # 부분집합의 원소로 참여시키지 않는 경우


if __name__ == "__main__":
    c, n = map(int, input().split())
    a = [0]*n  # 바둑이의 각각의 무게를 저장할 리스트
    result = -214700000
    for i in range(n):
        a[i] = int(input())
    total = sum(a)
    DFS(0, 0, 0)
    print(result)