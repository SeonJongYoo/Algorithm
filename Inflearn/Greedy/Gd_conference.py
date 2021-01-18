# 그리디 알고리즘 - 회의실 배정

# 내가 작성한 코드
N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr = sorted(arr, key=lambda x: x[1]) # 끝나는 시간에 맞춰서 오름차순 정렬

k = 0
cnt = 1
for j in range(1, N):
    if arr[k][1] <= arr[j][0]:
        cnt += 1
        k = j

print(cnt)

# 강의 코드
n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e)) # 튜플 형태로 리스트에 데이터를 입력
meeting.sort(key=lambda x: (x[1], x[0]))
et = 0 # 끝나는 시간 기록
cnt = 0
for s, e in meeting:
    if s >= et:
        et = e
        cnt += 1
print(cnt)
