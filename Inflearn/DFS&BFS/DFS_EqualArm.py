# 양팔 저울


# 내가 작성한 코드
# 정답은 맞으나 time error가 계속 발생함 - 모든 물의 무게에 대해서 각각 연산을 수행함
# 따라서, 물의 무게 개수가 많을수록 시간복잡도는 증가함!!!!!!
def DFS(L, s, p):
    global cnt, ck
    if L == p:  # p: 뽑을 추의 갯수
        if res[0] > sum(res) - res[0]:
            return
        DFS2(0, 0)
    else:
        # 모든 추의 무게를 다 넣어보아야 한다.
        # 뽑은 추와 물의 무게를 비교 - 물에 추를 넣어서 비교하기도 해야한다.
        # 물의 무게와 뽑은 추의 무게를 가지고 조합을 구한다. - 합이 같은 조합이 있으면 w리스트에 1로 체크
        ck = False
        for i in range(s, k+1):
            if ch[i] == 0:
                if ck:
                    break
                ch[i] = 1
                res.append(choo[i])
                DFS(L+1, i+1, p)
                res.pop()
                ch[i] = 0


# 위에서 구성한 res리스트에서 합이 같은 부분집합 찾기
def DFS2(v, Sum):
    global ck, cnt
    if v == len(res):
        if Sum == sum(res) - Sum:
            cnt += 1
            w[res[0]] = 1
            ck = True
            return
    else:
        if ck:  # 현재 물의 무게로 측정이 가능하다면 return
            return
        DFS2(v+1, Sum + res[v])
        DFS2(v+1, Sum)


if __name__ == "__main__":
    k = int(input())
    choo = list(map(int, input().split()))
    choo.insert(0, 0)
    w = [0] * (sum(choo) + 1)
    ch = [0] * (k + 1)  # 추의 무게별 사용을 체크하는 리스트
    res = []
    cnt = 0
    ck = False
    for y in range(1, len(w)):
        for x in range(1, k+1):  # 뽑을 추의 개수: 1개 뽑는 경우, 2개 뽑는 경우, 3개 ...
            if w[y] == 1:
                break
            res.append(y)
            DFS(0, 1, x)
            res.pop()
    cnt = len(w) - cnt - 1
    print(cnt)


# 강의 코드
# 상태트리 구성 - 추를 저울에 왼쪽에 놓는 경우(추의 무게를 더해준다), 오른쪽에 놓는 경우(추의 무게를 빼준다), 놓지 않는 경우
# 상태트리 구성을 잘 생각해보자!!!! - edge를 뻗을 때 각각 무엇을 의미하는지
# ****모든 물의 무게를 다 검색하는 것이 아니라 추의 무게를 가지고 측정 가능한 물의 무게를 계산해야 한다.****
# 무게가 음수가 되는 경우는 그릇이 왼쪽에 놓이는 경우이다. - 양수일 때 그릇은 오른쪽에 놓는다.
# 대칭으로 같은 경우가 발생한다. - -4와 4는 같은 경우이다.
# 따라서, 음수인 경우는 굳이 체크하지 않아도 된다. 어차피, 양수인 경우에서 같은 케이스가 발생하기 때문에
def DFS(L, Sum):  # L: 현재 추의 무게
    global res
    if L == n:
        if 0 < Sum <= s:  # 대칭구조가 항상 발생하기 때문에 음수인 경우는 굳이 체크하지 않는다.
            res.add(Sum)  # res를 set으로 선언한 이유: Ng의 물을 측정하기 위한 방법이 여러 개 존재하는데
            # Ng을 측정할 수 있는 방법 1개만 찾으면 된다.
    else:
        DFS(L+1, Sum+G[L])  # 추를 왼쪽에 놓는 경우
        DFS(L+1, Sum-G[L])  # 추를 오른쪽에 놓는 경우
        DFS(L+1, Sum)  # 추를 저울에 놓지 않는 경우
        

if __name__ == "__main__":
    n = int(input())
    G = list(map(int, input().split()))
    s = sum(G) 
    res = set()  # set() 모듈 사용!!! - set은 중복을 제거한다.
    DFS(0, 0)
    print(s - len(res))  # 측정이 블가능한 무게의 개수 = 전체 물의 무게의 개수 - 측정 가능한 무게의 개수
