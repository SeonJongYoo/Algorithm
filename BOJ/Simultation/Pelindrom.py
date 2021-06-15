# 펠린드롬인지 확인하기
'''s = input()
for i in range(len(s)//2):
    if s[i] != s[len(s)-i-1]:
        print(0)
        exit(0)
print(1)'''

n = input()
l = len(n)
res = 0
for i in range(l-1, -1, -1):
    if ord(n[i]) > 64:
        res += (ord(n[i]) - 55)*(16**(l-i-1))
    else:
        res += int(n[i])*(16**(l-i-1))
print(res)
'''if s == s[::-1]:
    print(1)
else:
    print(0)'''