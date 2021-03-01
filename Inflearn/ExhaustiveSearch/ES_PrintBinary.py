# 재귀함수를 이용한 이진수 출력


# 내가 작성한 코드
def DFS(N, r):
    r += str(N % 2)  # 나머지
    n = N // 2  # 몫
    if n == 1:
        r += "1"
        return r
    else:
        result = DFS(n, r)

    return result


if __name__ == "__main__":
    n = int(input())
    tmp = ""
    res = DFS(n, tmp)
    print(res[::-1])


# 강의 코드
# Stack 활용
def DFS(x):
    if x == 0:
        return  # return이 실행되면 스택에서 pop된다.
    else:
        DFS(x//2)  # 스택에 계속 push됨 - D(11)-30번 line, D(5)-30번 line, D(2)-30번 line, D(1)-30번 line, D(0)-return
        print(x % 2, end='')

if __name__ == "__main__":
    n = int(input())
    DFS(n)