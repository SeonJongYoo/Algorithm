# 최대 부분 증가수열 - BottomUp

n = int(input())
arr = list(map(int, input().split()))
# 주어진 상황을 아주 간단하게 생각하고 전체 경우에 대해 생각한다.
# arr의 각 원소들이 부분증가수열의 마지막 항일 경우를 생각하고 dy를 정의한다.
# dy의 각 원소들이 무엇을 의미하는지 정의하기
# dy[1]: arr[1]이 만들고자 하는 부분증가수열의 마지막 항일 때 부분증가수열의 최대길이
dy = [0] * n
dy[0] = 1
for i in range(1, n):
    for j in range(i-1, -1, -1):
        if arr[i] > arr[j]:
            if dy[i] < dy[j] + 1:  # 최댓값 판별.
                # i번째에 해당하는 원소를 추가하므로 길이에 1을 더해준다.
                dy[i] = dy[j] + 1
    if dy[i] == 0:
        dy[i] = 1
print(max(dy))