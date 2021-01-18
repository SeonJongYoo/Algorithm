# 뮤직비디오 - 결정 알고리즘
# lt, rt, mid를 정해주기 위한 범위를 생각하는 것이 핵심!

# 내가 작성한 코드
def Count(size):
    cnt = 0
    sum = 0
    for i in range(n):
        sum += song[i]
        if sum > size:  # 현재 용량(mid)을 기준으로 곡의 용량을 합하여 DVD에 담는다.
            cnt += 1
            sum = 0
            sum += song[i]
    cnt += 1
    return cnt

n, m = map(int, input().split())
song = list(map(int, input().split()))
maxx = max(song)  # DVD의 용량은 부른 곡들 중에 하나는 무조건 담을 수 있어야하므로
# DVD의 최소 용량은 부른 곡의 최댓값이다.
# DVD 용량의 범위는 부른 곡의 최댓값 ~ 부른 곡의 길이의 합(주어진 리스트의 총합)이다.
lt = maxx  # lt는 부른 곡 중 최대 길이
rt = sum(song)  # rt는 부른 곡들의 합(주어진 리스트의 총합)
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) <= m:  # 현재 용량(mid)을 기준으로 DVD의 개수를 계산했을 때 M보다 작다면 현재 용량이
        # 너무 커서 DVD의 개수가 작게 계산된 것으로 현재 용량을 줄이기 위해 rt = mid-1로 현재 용량을 계산한다.
        # 현재 용량(mid)이 답이 될 수 있다면 현재 용량보다 큰 값은 모두 답이 될 수 있다는 것을 의미!
        res = mid
        rt = mid - 1   # M과 같다면 현재 용량이 가장 작아질 때까지 계산을 반복한다.
    else:
        lt = mid + 1
print(res)


# 강의 코드 - 내가 작성한 코드와 동일한 의미
def Count(capacity):
    cnt = 1
    sum = 0
    for x in Music:
        if sum + x > capacity:  # sum : 하나의 DVD에 저장된 곡들의 시간의 합
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt

n, m = map(int, input().split())
Music = list(map(int, input().split()))
maxx = max(Music)
lt = 1
rt = sum(Music)
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if mid >= maxx and Count(mid) <= m:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(res)