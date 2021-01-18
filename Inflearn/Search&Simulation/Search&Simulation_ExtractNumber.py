# 숫자만 추출

# 내가 작성한 코드
s = input()
length = len(s)
num = []
for i in range(length):
    if s[i].isdigit():
        num.append(s[i])
res = ""
if num[0] == '0':
    for i in range(1, len(num)):
        res += num[i]
else:
    for i in range(len(num)):
        res += num[i]
res = int(res)
print(res)

cnt = 1
for i in range(2, res+1):
    if res % i == 0:
        cnt += 1
print(cnt)

# 강의 코드
s = input()
res = 0
for x in s:  # 문자열 s의 문자 하나하나에 접근 가능!!
    if x.isdecimal():  # isdigit(): x가 숫자인지 판단. isdecimal(): 0~9사이 숫자인지 판단
        res = res * 10 + int(x)  # 표현 방법 기억하기. 연산을 진행할수록 자릿수를 증가하여 더함
        # 처음: res는 일의 자리, 두 번째: res는 십의 자리, ...
print(res)

cnt = 0
for i in range(1, res+1):  # 약수 구하기
    if res % i == 0:
        cnt += 1
print(cnt)