# 합이 같은 부분집합(DFS)


# 내가 작성한 코드

# 서로소라는 조건을 굳이 체크할 필요 없다고 생각하고 구현함
# 합이 같은 경우는 YES를 출력하고 exit(0)함수를 통해 프로그램을 강제종료 시킴
# NO인 경우 DFS함수의 return값이 None이 되기 때문에 YES와 구분하였다.
def DFS(v):
    if v == n:
        larr = []
        rarr = []
        for i in range(1, arr[n-1]+1):
            if ch[i] == 1:
                #print(i, end=' ')
                larr.append(i)
            else:
                if i in arr:
                    rarr.append(i)
        #print()
        if sum(larr) == sum(rarr):
            print("YES")
            exit(0)
        else:
            return
    else:
        ch[arr[v]] = 1
        DFS(v+1)
        ch[arr[v]] = 0
        DFS(v+1)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ch = [0] * (arr[n-1]+1)  # 주어진 집합의 최댓값을 구하여 그만큼의 크기로 ch리스트를 선언한다.
    x = DFS(0)
    if x is None:
        print("NO")


# 강의 코드
# 전체 집합의 합에서 현재 구한 하나의 부분집합의 합을 뺐을 때
# 현재 구한 부분집합의 합과 같은지를 확인하여 두 부분집합의 합을 비교한다.
# 시간복잡도 줄이기
# 두 부분집합의 합이 같으려면 하나의 부분집합에서 원소들의 합이 total의 절반을 넘어가면 안된다!
import sys
def DFS(L, sum):  # L은 a리스트의 index를 나타냄
    if sum > total // 2:  # total의 절반을 넘어가는 경우, 어차피 NO이므로 return해버린다.
        return
    if L == n:  # 종료지점
        if sum == (total-sum):
            print("YES")
            sys.exit(0)  # 내가 작성한 코드와 같은 방식!!!
    else:
        DFS(L+1, sum+a[L])  # 현재 원소를 부분집합으로 사용하는 경우 - 그 원소를 더해준다
        DFS(L+1, sum)  # 현재 원소를 부분집합으로 사용하지 않는 경우 - 그 원소를 더하지 않고 넘어간다.

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)  # 전체 집합의 원소들의 합
    DFS(0, 0)
    print("NO")  # YES인 경우 프로그램이 강제 종료되므로 이렇게 작성하여도 상관없다.

