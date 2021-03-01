# 이진트리순회


# 깊이 우선탐색이나 완전탐색 구현시 기본 구조 - if else문
# 스택 활용
def DFS(v):
    if v > 7:
        return
    else:
        # 전위순회
        print(v, end=' ')
        DFS(v*2)  # 왼쪽 자식노드 호출
        DFS(v*2 + 1)  # 오른쪽 자식노드 호출

        # 중위순회
        DFS(v*2)
        print(v, end=' ')
        DFS(v*2 + 1)

        # 후위순회
        DFS(v*2)
        DFS(v*2 + 1)
        print(v, end=' ')

if __name__ == "__main__":
    DFS(1)