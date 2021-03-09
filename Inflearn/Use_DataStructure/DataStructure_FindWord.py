# 단어찾기 - 해쉬

# 강의 코드
n = int(input())
p = dict()
for i in range(n):  # 노트에 미리 적어놓은 단어
    word = input()
    p[word] = 1
for i in range(n-1):  # 시에 실제로 쓰인 단어
    word = input()
    p[word] = 0

# p.items(): dictionary에 있는 데이터(key, value)에 하나씩 접근
# dictionary는 key와 value를 동시에 접근 가능하다.
for key, value in p.items():
    if value == 1:
        print(key)
        break
