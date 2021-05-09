# 듣보잡


# 내가 작성한 코드
# 듣도 못한 명단과 보도 못한 명단의 스택을 각각 생성하고 입력으로 들어오는 이름을 서로 비교하여
# 서로 다르면 스택에 push, 같으면 res리스트에 append한다.
# 서로 다른 경우 스택에 push하기 전에 서로 반대편 스택의 top을 확인하고 같으면 pop! 다르면 push!
# top과 비교하게 되면 반대편 스택에 같은 이름이 있어도 pop을 할 수 없게됨!
# 답이 틀림
'''n, m = map(int, input().split())
name1 = []
name2 = []
for _ in range(n):
    name1.append(input())
for _ in range(m):
    name2.append(input())
name1.sort()
name2.sort()
print(name1)
print(name2)
s1 = []
s2 = []
res = []
i1, i2 = 0, 0
while i1 < len(name1) or i2 < len(name2):
    if i1 < len(name1) and i2 < len(name2):
        if name1[i1] != name2[i2]:
            if s1 and s1[len(s1)-1] == name2[i2]:
                s1.pop()
                s1.append(name1[i1])
                res.append(name2[i2])
            elif s2 and s2[len(s2)-1] == name1[i1]:
                s2.pop()
                s2.append(name2[i2])
                res.append(name1[i1])
            else:
                s1.append(name1[i1])
                s2.append(name2[i2])
        else:
            res.append(name1[i1])
    elif i1 < len(name1):
        if s2 and s2[len(s2) - 1] == name1[i1]:
            s2.pop()
            res.append(name1[i1])
    elif i2 < len(name2):
        if s1 and s1[len(s1) - 1] == name2[i2]:
            s1.pop()
            res.append(name2[i2])
    #print("s1: ", s1)
    #print("s2: ", s2)
    i1 += 1
    i2 += 1
print(len(res))
#res.sort()
for x in res:
    print(x)'''

# 내가 작성한 코드2
# 반대편 스택의 top과 비교하는 것이 아니라 리스트 전체를 탐색
# -> 시간초과 발생!
'''n, m = map(int, input().split())
name1 = []
name2 = []
for _ in range(n):
    name1.append(input())
for _ in range(m):
    name2.append(input())
name1.sort()
name2.sort()
#print(name1)
#print(name2)
s1 = []
s2 = []
res = []
i1, i2 = 0, 0
while i1 < len(name1) or i2 < len(name2):
    if i1 < len(name1) and i2 < len(name2):
        if name1[i1] != name2[i2]:
            if s1 and name2[i2] in s1:  # 반대편 스택 전체를 탐색! - 시간초과
                s1.pop()
                s1.append(name1[i1])
                res.append(name2[i2])
            if s2 and name1[i1] in s2:
                s2.pop()
                s2.append(name2[i2])
                res.append(name1[i1])
            else:
                s1.append(name1[i1])
                s2.append(name2[i2])
        else:
            res.append(name1[i1])
    elif i1 < len(name1):
        if s2 and name1[i1] in s2:
            s2.pop()
            res.append(name1[i1])
    elif i2 < len(name2):
        if s1 and name2[i2] in s1:
            s1.pop()
            res.append(name2[i2])
    #print("s1: ", s1)
    #print("s2: ", s2)
    i1 += 1
    i2 += 1
print(len(res))
#res.sort()
for x in res:
    print(x)'''


# 내가 작성한 코드3 - 이분 탐색
n, m = map(int, input().split())
name1 = []
name2 = []
for _ in range(n):
    name1.append(input())
for _ in range(m):
    name2.append(input())
name1.sort()
name2.sort()
res = []
for target in name2:
    st = 0
    ed = len(name1) - 1
    while st <= ed:
        mid = (st + ed) // 2
        if name1[mid] == target:
            res.append(target)
            break
        elif name1[mid] > target:
            ed = mid-1
        else:
            st = mid+1
print(len(res))
#res.sort()
for x in res:
    print(x)