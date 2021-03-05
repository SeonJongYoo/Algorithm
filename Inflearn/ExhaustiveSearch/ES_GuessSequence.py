# 수열 추측하기


# 내가 작성한 코드
# 주어진 마지막 숫자 F를 1, 2, 3 ...F-1까지 차례대로 분할하려했다.
# 짝수번째 level(0, 2, 4, ...)에서는 원소의 갯수가 홀수개 존재하는데 내가 생각한 알고리즘에서
# temp리스트를 통해 결합할 때 앞 리스트의 맨 뒤 숫자와 뒤 리스트의 맨 앞 숫자가 같다면
# 가운데 숫자가 공통이다는 의미이므로 같지 않는 경우는 연산을 수행하지 않도록 한다.
# ***********************문제 이해를 잘못했다!!*********************
'''def DFS(L, F): - 오답. 완전 오답
    global ck
    temp = []
    if L == n:
        print(res)
    else:
        for i in range(1, F+1):
            if F - i < 1:
                print("XXXXXX")
                ck = True
                return
            print("L, i:  ", L, i)
            temp.append(i)
            temp.append(F-i)
            print("temp: ", temp)
            if L > 0 and L % 2 == 0:
                if len(res) == L+1 and res[L].pop() == i:
                    res[L].append(F-i)
                # 처음거와 두번째거 어떻게 구분하지
                # 처음엔 res리스트가 비어있음. 두번째는 res리스트가 채워져있음.
                # 지금 알고리즘은 res리스트가 L번째에서 비어있다면 처음인지 두번째인지 구분없이 무조건
                # return한다.
                # 지금 알고리즘은 처음엔 채우지 않고 두번째에 채우는 경우만 구분한다.
                elif ck:
                    print("HERE!!!!!!")
                    ck = False
                    return
            res.append(temp)
            print("res: ", res)
            DFS(L+1, i)
            ck = False
            DFS(L+1, F - i)
            ck = False
            res.pop(L)
            temp.clear()


if __name__ == "__main__":
    n, f = map(int, input().split())
    # n이 의미하는 것은 수열 첫 번째 층의 숫자들이 각각1 ~ n 중에 하나이고 총 n개임을 의미한다.
    res = [[f]]
    ck = False
    DFS(1, f)'''


# 내가 작성한 코드2 - 정답
# 마지막 층의 값은 첫번째 층의 숫자들에 이항계수를 적용하여 계산된 것이다.
# n = 3: 1 2 1
# n = 4: 1 3 3 1
# n = 5: 1 4 6 4 1
# n = 6: 1 5 10 10 5 1
def DFS(L):
    global Sum, Min, result
    if L == n:
        #print(res)
        temp = []
        while L > 1:
            if L == n:
                for j in range(L-1):
                    temp.append(res[j] + res[j + 1])
            else:
                for j in range(L-1):
                    temp[j] = temp[j] + temp[j+1]
                temp.pop()
            #print("temp: ", temp)
            L -= 1
        if temp[0] == f:
            for i in range(n):
                print(res[i], end=' ')
            exit(0)
        #print("MIN: ", Min)
        #print("RESULT: ", result)
        #print("-------------------------")
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                res[L] = i
                ch[i] = 1
                DFS(L+1)
                ch[i] = 0


if __name__ == "__main__":
    n, f = map(int, input().split())
    # n이 의미하는 것은 수열 첫 번째 층의 숫자들이 각각 1 ~ n 중에 하나이고 총 n개임을 의미한다.
    res = [0] * n
    ch = [0] * (n+1)
    Sum = 0
    #Min = 2147000000
    result = []
    DFS(0)


# 강의 코드
# 마지막 층의 값은 첫번째 층의 숫자들에 이항계수를 적용하여 계산된 것이다.
# n = 3: 1 2 1
# n = 4: 1 3 3 1
# n = 5: 1 4 6 4 1
# n = 6: 1 5 10 10 5 1
def DFS(L, Sum):
    if L == n and sum == f:
        for x in p:
            print(x, end=' ')
        exit(0)
    else:
        # 순열 만들기
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                p[L] = i
                DFS(L+1, Sum + (p[L] * b[L]))  # 이항계수 b리스트와 바로 연산 - 1x3 + 3*1 + 3*2 + 1*4
                ch[i] = 0  # 함수가 종료됐을 때 다시 원상복구 시켜야함


if __name__ == "__main__":
    n, f = map(int, input().split())
    # n이 의미하는 것은 수열 첫 번째 층의 숫자들이 각각 1 ~ n 중에 하나이고 총 n개임을 의미한다.
    p = [0] * n  # p에 순열들을 만들어 나간다.
    b = [1] * n  # 이항계수 초기화 리스트
    ch = [0] * (n + 1)

    # 각 차수마다 이항계수 구하기
    for i in range(1, n):
        b[i] = b[i-1] * (n-i) // i  # 조합 계산 - 분자는 이전 항의 계수에 n-1을 곱하고
        # 현재 항의 분모는 연산을 진행할 때마다 이전 항의 분모의 값(1)에서 1씩 증가한 값(2)을
        # 이전 항의 분모(1)에 곱해준다 ---> 현재항의 분모: 1x2
    DFS(0, 0)


# 강의 코드2 - 참고사항
# 라이브러리 사용 - 순열과 조합을 자동으로 계산해줌
import itertools as it  # 순열과 조합을 계산
n, f = map(int, input().split())
b = [1] * n
for i in range(1, n):
    b[i] = b[i - 1] * (n - i) // i

a = list(range(1, n+1))  # 1 ~ n까지의 숫자들
# 순열 라이브러리
for tmp in it.permutations(a):  # a에 있는 숫자들에 대해 모든 순열을 계산한다.
    print(tmp)
for tmp in it.permutations(a, 3):  # a에 있는 숫자들 중에서 3개를 뽑아 모든 순열을 계산한다.
    print(tmp)


# 문제에 라이브러리 적용한 코드
for tmp in it.permutations(a):
    Sum = 0
    for L, x in enumerate(tmp):  # L은 이항계수 b리스트에 접근하기 위한 것
        Sum += (x * b[L])
    if Sum == f:
        for x in tmp:
            print(x, end=' ')
        break  # 가장 첫번째 for문을 정지한다. - 더 이상 순열을 검색하지 않음
