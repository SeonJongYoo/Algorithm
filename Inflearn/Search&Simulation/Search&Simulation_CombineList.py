# 두 리스트 합치기

# 내가 작성한 코드
'''n = int(input())
list_n = list(map(int, input().split()))
m = int(input())
list_m = list(map(int, input().split()))

for i in range(len(list_m)):
    list_n.append(list_m[i])
list_n.sort()

for i in list_n:
    print(i, end=' ')'''


# 수정 코드
n = int(input())
list_n = list(map(int, input().split()))
m = int(input())
list_m = list(map(int, input().split()))
p1, p2 = 0, 0
new = []
check = 0
while True:
    if list_n[p1] > list_m[p2]:
        new.append(list_m[p2])
        p2 += 1
    else:
        new.append(list_n[p1])
        p1 += 1
    if p1 > n - 1:
        check = p1
        break
    elif p2 > m - 1:
        check = p2
        break
if check == p1:
    for i in range(p2, m):
        new.append(list_m[i])
else:
    for i in range(p1, n):
        new.append(list_n[i])

for x in new:
    print(x, end=' ')


# 강의 코드
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
p1 = p2 = 0
c = []
while p1 < n and p2 < m:
    if a[p1] < b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1
if p1 < n:
    c = c + a[p1:]  # a[p1]: a리스트의 p1부터 끝까지를 나타냄. for문보다 빠름
if p2 < m:
    c = c + b[p2:]  # b[p2]: b리스트의 p2부터 끝까지를 나타냄. for문보다 빠름

for x in c:
    print(x, end=' ')