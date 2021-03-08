# 아나그램 - 딕셔너리 해쉬

# dictionary의 key는 알파벳, value는 알파벳의 개수
# key가 동일한 경우 value를 누적해야함
# dictionary 내장 함수 get('A', 0): key값 'A'에 value가 존재하면
# 그 value를 가져오고 없으면 0을 가져온다.

# 강의 코드
a = input()
b = input()
str1 = dict()
str2 = dict()
for x in a:
    str1[x] = str1.get(x, 0) + 1
for x in b:
    str2[x] = str2.get(x, 0) + 1

for i in str1.keys():
    if i in str2.keys():  # str1의 key값이 str2에 있는지 확인
        if str1[i] != str2[i]:  # str2에도 같은 key값이 존재한다면 value를 비교했을 때 같지 않은 경우
            print("NO")
            break
    else:  # str1의 key값이 str2에 없는 경우
        print("NO")
        break
else:  # str1의 key값이 str2에 존재하고 value도 같은 경우
    print("YES")

# 강의 코드 개선
a = input()
b = input()
sH = dict()
for x in a:  # a문자열을 읽으면서 sH의 각 key(알파벳)의 value들을 1씩 증가시킴
    sH[x] = sH.get(x, 0) + 1

for x in b:  # b문자열을 읽으면서 sH의 각 key(알파벳)의 value들을 1씩 감소시킴
    sH[x] = sH.get(x, 0) - 1
# 아나그램이라면 sH의 모든 value는 0이 된다.
# 아나그램이 아니라면 sH의 value 중 0이 아닌 것이 존재한다.
for x in a:
    if sH.get(x) > 0:
        print("NO")
        break
else:
    print("YES")