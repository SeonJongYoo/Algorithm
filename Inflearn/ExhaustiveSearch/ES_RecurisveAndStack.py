# 재귀함수와 스택
# 함수 호출시 함수의 호출정보가 스택에 push됨
# 이때, 함수를 또 호출하면 현재 위치의 정보를 스택의 top에 기록하고 새로 호출된 함수의 정보를 스택에 push함


def DFS(x, r):
    if x >= 0:
        if x == 0:
            return
        r = str(x % 2)
        x = x // 2
        DFS(x, r)
        print(r, end='')


if __name__=="__main__":
    n=int(input())
    res=""
    DFS(n, res)