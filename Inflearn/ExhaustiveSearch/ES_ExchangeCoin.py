# 동전교환


# 내가 작성한 코드
# 중복순열 문제와 같은 유형
# 합이 m을 넘어가는 경우 return되어 이전 순서로 돌아온 경우
# sum은 m을 넘어간 값을 유지하고 있기 때문에 이전에 더한 동전(coin[i-1])과 그 cnt를 빼고 다음 순번의 숫자를 더해주어야한다.
# ---> 현실적으로 불가능함. sum = sum - coin[i-1]을 해주는 경우 index에러 발생
def DFS(L, S):
    global cnt, Min
    suM = S
    if suM > m:
        return
    if cnt > Min:
        return
    if suM == m:
        if cnt != 0 and cnt < Min:
            Min = cnt
            cnt = 0
    else:
        for i in range(n):
            suM += coin[i]
            cnt += 1
            DFS(L+1, suM)


if __name__ == "__main__":
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())
    #ck = False
    cnt = 0
    Min = 10000000
    DFS(0, 0)
    print(Min)


# 내가 작성한 코드2
# 위에서 발생한 문제가 해결되지 않음
def DFS(L, S):  # L은 상태트리에서 level을 나타냄. L이 사용한 동전의 개수를 의미함
    # 따라서, level이 가장 작은 곳에서 답이 있음!
    global Min
    if S > m:
        return
    if L > Min:
        return
    if S == m:
        if L < Min:
            Min = L
            print("MIN: ", Min)
    else:
        for i in range(n):
            S += coin[i]
            print("S: ", S)
            print("L: ", L)
            DFS(L+1, S)


if __name__ == "__main__":
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    Min = 10000000
    DFS(0, 0)
    print(Min)


# 강의 코드
# 주어진 리스트를 역순으로 정렬하는 방법은 내가 작성한 코드와 일치함
# 역순으로 정렬하면 큰 동전부터 더하게되므로 동전의 개수는 줄어들게됨
# 추가적인 cut edge(시간복잡도 줄이기)가 필요함
def DFS(L, Sum):
    global res
    if L > res:  # 이미 구한 res보다 큰 동전의 개수는 굳이 연산을 계속할 필요가 없으므로 바로 return하여 시간 복잡도를 줄인다.
        return
    if Sum > m:  # cut edge - 동전의 합이 m보다 큰 경우는 굳이 연산을 계속할 필요가 없으므로 바로 return
        return
    if Sum == m:  # 종료지점 - 뽑은 동전의 합이 m과 같은 경우
        if L < res:
            res = L
            print("*****MIN: ", res)
    else:
        for i in range(n):
            print("L: ", L)
            print("Sum: ", Sum)
            # *******************
            DFS(L+1, Sum+a[i])  # 동전의 개수가 증가하면서 총 금액을 더해줘야하므로 Sum+a[i]로 작성한다.
            # 위의 식을 잘 기억하자!! - 내가 작성한 코드에서 발생한 문제가 아예 발생하지 않음!
            # ******************

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    m = int(input())
    res = 21470000000
    DFS(0, 0)
    print(res)
