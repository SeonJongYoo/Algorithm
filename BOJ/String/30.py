# 30


# 내가 작성한 코드 - Runtime Error.
# "N이 최대 100000개의 숫자로 구성되어 있다."
# 입력으로 들어온 숫자를 한 자리씩 파싱하여 리스트에 담는다.
# 리스트에 담긴 숫자들에 대해 순열 개념을 적용한다.
# 각 경우에 대해서 문제의 조건을 만족하는 경우를 찾는다.
'''def DFS(L):
    global Max, first
    if first > res[0]:
        return
    if L == cnt and res[0] != 0:
        print("res: ", res)
        num = 0
        for i in range(cnt):
            num += res[i]*pow(10, cnt-i-1)
        if num%30 == 0 and num > Max:
            first = res[0]
            Max = num
    else:
        for i in range(cnt):
            if ch[i] == 0:
                ch[i] = 1
                res[L] = n[i]
                DFS(L+1)
                ch[i] = 0
                res[L] = 0


n = list(map(int, input()))
cnt = len(n)
res = [0]*cnt
ch = [0]*cnt
Max = -1
first = 0
DFS(0)
print(Max)'''


# 내가 작성한 코드 2
# 문제 조건 - "30의 배수이다"라는 말이 중요하다.
# 30의 배수가 되기 위한 조건
# 1. 일의 자리 숫자가 항상 0이다. 2. 각 자리의 숫자의 합이 3의 배수
# 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, ...
n = list(map(int, input()))
n.sort(reverse=True) # 내림차순 정렬 - 최댓값을 구하기 위해, 일의 자리가 0인지 판단하기 위해
# 내림차순 정렬 후 값이 30의 배수가 되지 않아 숫자의 배치를 바꿔서 30의 배수가 될 가능성은 없다.
# 이미 현 숫자가 30의 배수이면 일의 자리를 0으로 유지한 채로 숫자의 배치를 바꿔도 30의 배수가 된다.
# 다시 말해, 현 숫자의 일의 자리가 0이지만 30의 배수가 아닌 경우 일의 자리를 0으로
# 유지한 채로 숫자의 배치를 바꿔도 30의 배수가 될 수 없다.
if n[len(n)-1] == 0 and sum(n)%3 == 0: # 30의 배수 판단
    res = 0
    for x in n:
        print(x, end="")
else:  # 내림차순 정렬 후 일의 자리가 0이 아니라는 것은 절대 30의 배수가 될 수 없다는 뜻
    print(-1)


