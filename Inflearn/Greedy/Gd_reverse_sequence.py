# 역수열 - 그리디 알고리즘
# 내가 작성한 코드 - 주어진 수열에서 가장 큰 값의 역수열은 항상 0이다.
# 최댓값이 8일 때 6의 역수열 개수가 1이라면 6은 8과 7 사이에 있다는 것을 의미한다.
N = int(input())
arr = list(map(int, input().split()))

seq = [N]
k = 1
for i in range(N-2, -1, -1):
    if arr[i] != 0:
        if arr[i] == k:
            seq.append(i+1)
        elif arr[i] < k:
            seq.insert(arr[i], i+1)
    else:
        seq.insert(0, i+1)
    k += 1

for i in range(N):
    print(seq[i], end=" ")

# 강의 코드
n = int(input())
a = list(map(int, input().split()))
seq = [0] * n
for i in range(n):
    for j in range(n):
        if a[i] == 0 and seq[j] == 0:
            seq[j] = i+1
            break
        elif seq[j] == 0:# a[i]가 0이 될 때까지 1을 빼주고 0이 되는 시점에 seq[j]에 값을 추가한다.
            a[i] -= 1
for x in seq:
    print(x, end=' ')
