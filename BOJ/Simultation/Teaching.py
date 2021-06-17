# 가르침


# anta, tica -> 5글자로 이루어짐. a, c, i, n, t
# k가 5개보다 작으면 학생들이 읽을 수 있는 단어가 없음
# 입력 순서대로 개수를 세면 안된다! - 뒷부분에 읽을 수 있는 단어가 여러 개 존재할 수 있음
# anta, tica를 제외한 단어들을 set을 통해 모으고 이를 리스트로 변환한 다음 배울 수 있는 글자 개수의 조합을 구한다.
# 구한 조합에 해당하는 글자는 1로 변경

# dictionary를 사용하여 포함 관계 확인
# combination 직접 구현
# python3 - 시간 초과 발생

'''import sys


def DFS(L, s):
    global Max
    if L == rcnt:
        res, t = 0, 0
        for k in tList:
            dic[k] = 1
        for x in words:
            if res + len(words) - t <= Max:
                break
            t += 1
            tmp = set(x)
            flag = False
            for y in tmp:
                if dic[y] == 0:
                    flag = True
                    break
            if flag:
                continue
            res += 1
        if res > Max:
            Max = res
        for k in tList:
            dic[k] = 0
    else:
        for k in range(s, len(List)):
            tList.append(List[k])
            DFS(L+1, k+1)
            tList.pop()


n, k = map(int, sys.stdin.readline().split())
dic = {}
for i in range(26):
    if chr(i+97) == 'a' or chr(i+97) == 'c' or chr(i+97) == 'i' or chr(i+97) == 'n' or chr(i+97) == 't':
        dic[chr(i+97)] = 1
    else:
        dic[chr(i+97)] = 0
cnt = 5
words = []
Set = set()
for _ in range(n):
    w = sys.stdin.readline().rstrip()
    twords = []
    for j in range(4, len(w)-4):
        twords.append(w[j])
        if dic[w[j]] == 0:
            Set.add(w[j])
    words.append(twords)
List = list(Set)
tList = []
rcnt = k-5
res = 0
Max = 0
if rcnt >= 0:
    if rcnt >= len(List):
        Max = n
    else:
        DFS(0, 0)
print(Max)'''


# dictionary를 사용하여 포함 관계 확인
# combination 라이브러리 사용
# pypy3 - 통과
'''import sys
import itertools as it

n, k = map(int, sys.stdin.readline().split())
dic = {}
for i in range(26):
    if chr(i+97) == 'a' or chr(i+97) == 'c' or chr(i+97) == 'i' or chr(i+97) == 'n' or chr(i+97) == 't':
        dic[chr(i+97)] = 1
    else:
        dic[chr(i+97)] = 0
cnt = 5
words = []
Set = set()
for _ in range(n):
    w = sys.stdin.readline().rstrip()
    twords = []
    for j in range(4, len(w)-4):
        twords.append(w[j])
        if dic[w[j]] == 0:
            Set.add(w[j])
    words.append(twords)
List = list(Set)
rcnt = k-5
res = 0
Max = 0
if rcnt >= 0:
    if rcnt >= len(List):
        Max = n
    else:
        tList = it.combinations(List, rcnt)
        for temp in tList:
            res, t = 0, 0
            temp1 = list(temp)
            for k in temp1:
                dic[k] = 1
            for x in words:
                if res + len(words) - t <= Max:
                    break
                t += 1
                flag = False
                for y in x:
                    if dic[y] == 0:
                        flag = True
                        break
                if flag:
                    continue
                res += 1
            if res > Max:
                Max = res
            for k in temp1:
                dic[k] = 0
print(Max)'''


# 비트 마스크 - 시간 초과
# 현재 알고 있는 글자를 가지고 남극에 존재하는 단어들을 읽을 수 있는지 판단
# 현재 알고 있는 글자들을 이진수로 변경 - A
# 남극에 존재하는 단어들을 set을 통해 글자들로 추려내고 이를 이진수로 변경 - B
# A와 B 사이에 다른 것이 존재하면 안된다. -> A와 B의 비트 연산을 통해 다른 것을 찾아야 한다.
# AND 연산을 수행하여 0이 나오면 서로 다르다는 것을 알 수 있음!
# 문자에 대한 이진수 변경을 위해 문자를 아스키 코드로 변경 후 이진수로 변경한다.
import sys


# combination을 통해 anta tica를 제외한 글자들 중에서 배울 수 있는 글자(k-5개)를 추출
def DFS(L, s):
    global base, Max
    if L == rcnt:
        res = 0
        for i in range(n):
            if words[i] & base == words[i]:
                res += 1
        Max = max(res, Max)
    else:
        for i in range(s, len(List)):
            base |= 1 << (ord(List[i]) - ord('a'))
            DFS(L+1, i+1)
            base &= ~(1 << (ord(List[i]) - ord('a')))


n, k = map(int, sys.stdin.readline().split())
cnt = 5
default = ['a', 'c', 'i', 'n', 't']
base = 0 # anta tica를 이진수로 변경한 값
# a ~ z에 해당하는 문자를 0 ~ 25 사이에 해당하는 숫자로 변경
for i in default:
    num = ord(i) - ord('a')
    base |= 1 << num
Set = set()
words = []
for _ in range(n):
    w = sys.stdin.readline().rstrip()  # 남극에 존재하는 단어
    # *****************************************
    # 여기서 anta tica에 해당하지 않는 글자들만 추출하여 미리 2진수로 변경한다.
    tnum = 0
    for x in w[4:-4]:  # anta tica를 제외한 글자들만 추출하여 Set에 저장
        if x not in default:
            Set.add(x)
            tnum |= 1 << (ord(x) - ord('a'))
    words.append(tnum)
    # *******************************************
List = list(Set)  # anta tica를 제외하고 배울 수 있는 글자들
rcnt = k-5
Max = 0
if rcnt >= 0:
    if rcnt >= len(List):
        # anta tica를 제외하고 배울 수 있는 글자의 개수가 anta tica를 제외하고 현재 남극에 존재하는 글자의 개수보다 많은 경우
        Max = n
    else:
        DFS(0, 0)
print(Max)


# 비트 마스크 사용 - 성공!!
# combination 라이브러리 사용
'''import sys
import itertools as it


n, k = map(int, sys.stdin.readline().split())
cnt = 5
default = ['a', 'c', 'i', 'n', 't']
base = 0  # anta tica를 이진수로 변경한 값
for x in default:
    num = ord(x) - ord('a')
    base |= 1 << num
Set = set()  # anta tica를 제외하고 배울 수 있는 글자들
words = []
for _ in range(n):
    w = sys.stdin.readline().rstrip()  # 남극에 존재하는 단어
    tnum = 0
    for x in w[4:-4]:  # anta tica를 제외한 글자들만 추출
        if x not in default:
            Set.add(ord(x) - ord('a'))  # a ~ z의 문자를 0 ~ 25 사이에 해당하는 값으로 변경
            tnum |= 1 << (ord(x) - ord('a'))
    words.append(tnum)
rcnt = k-5
Max = 0
if rcnt >= 0:
    if rcnt >= len(Set):
        # anta tica를 제외하고 배울 수 있는 글자의 개수가 anta tica를 제외하고 현재 남극에 존재하는 글자의 개수보다 많은 경우
        Max = n
    else:
        tList = it.combinations(Set, rcnt)
        for x in tList:
            res = 0
            tbase = base
            for y in x:
                tbase |= 1 << y
            for k in range(n):
                if words[k] & tbase == words[k]:
                    res += 1
            Max = max(res, Max)
print(Max)'''