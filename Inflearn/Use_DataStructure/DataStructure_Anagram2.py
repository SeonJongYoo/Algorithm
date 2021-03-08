# 아나그램 - 리스트 해쉬

# 내가 작성한 코드
# 해싱을 이용한 것은 아님
a = list(input())
b = list(input())
sH = []
for x in b:
    if x in a:
        sH.append(x)  # b문자열을 하나씩 읽으면서 그것이 a에 존재하면 a문자열 리스트에서 삭제
        a.remove(x)   # 중복이 제거됨
    else:
        print("NO")
        break
else:
    print("YES")


# 강의 코드
# ascii 코드 이용 - A: 65 - Z: 90, a: 97 - z: 122
a = list(input())
b = list(input())
str1 = [0]*52
str2 = [0]*52
for x in a:
    if x.isupper():  # x가 대문자인지 판단 - 참이면 true리턴
        str1[ord(x) - 65] += 1  # x가 대문자이면 65를 빼서 st1리스트의 0번 index부터 해싱
    else:  # x가 소문자이면 71를 빼서 str1리스트의 26번 index부터 해싱
        str1[ord(x) - 71] += 1
for x in b:
    if x.isupper():
        str2[ord(x) - 65] += 1
    else:
        str2[ord(x) - 71] += 1
'''if str1 == str2:
    print("YES")
else:
    print("NO")'''
for i in range(52):
    if str1[i] != str2[i]:  # 알파벳의 개수를 비교
        print("NO")
        break
else:
    print("YES")