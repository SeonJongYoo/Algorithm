# 합이 같은 부분집합(DFS)
def DFS(L):
    if L == n:
        Sum = 0
        for i in range(n):
            if ch[i] == 1:
                Sum += arr[i]
        if Sum == total - Sum:
            print("YES")
            exit(0)
    else:
        ch[L] = 1
        DFS(L+1)
        ch[L] = 0
        DFS(L+1)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    total = sum(arr)
    ch = [0]*n
    DFS(0)
    print("NO")