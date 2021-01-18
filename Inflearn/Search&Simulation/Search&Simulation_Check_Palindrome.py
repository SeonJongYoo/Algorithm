# 회문 문자열 검사

# 내가 작성한 코드
n = int(input())
for i in range(1, n+1):
    flag = True
    string = input()
    string = string.upper()  # 중요: 대소문자 구분이 없으므로 모두 대문자나 소문자로 변경
    length = len(string)
    for j in range(length//2):
        if string[j] != string[length-1-j]:
            print(string[j], string[length - j - 1])
            flag = False
            break

    if flag is True:
        print('#%s'%(i), 'YES')
    else:
        print('#%s'%(i), 'NO')

# 강의 코드 - 직접 구현
n = int(input())
for i in range(n):
    s = input()
    s = s.upper()  # 대소문자를 구분하지 않으므로 모두 대문자나 소문자로 바꿔버린다.
    size = len(s)
    for j in range(size//2):
        if s[j] != s[-1 - j]:  # s[-1]은 s[size-1]와 같음
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))

    # for if else절: for문 내에 존재하는 if문에서 break에 걸리지 않으면 else문이 실행됨

# 강의 코드 - 간단한 풀이
n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    if s == s[::-1]:  # 입력받은 문자열을 뒤집음!. reverse
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" % (i + 1))