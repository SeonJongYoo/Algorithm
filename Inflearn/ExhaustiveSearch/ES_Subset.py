# 부분집합 구하기(DFS)


# 강의 코드
# 1부터 시작
# DFS의 인자를 부분집합으로 사용하는 경우와 사용하지 않는 경우를 나눈다.
# 사용하는 경우는 왼쪽 자식노드로 사용하지 않는 경우는 오른쪽 자식노드로 한다.
def DFS(v):
    if v == n+1:  # ch리스트의 원소가 1인 index만 출력
        for i in range(1, n+1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
    else:
        ch[v] = 1  # 원소v를 사용한다면 1
        DFS(v+1)
        ch[v] = 0  # 원소v를 사용하지 않는다면 0
        DFS(v+1)


if __name__ == "__main__":
    n = int(input())
    ch = [0]*(n+1)  # 원소를 부분집합으로 사용할지 안할지를 체크하는 리스트
    DFS(1)
