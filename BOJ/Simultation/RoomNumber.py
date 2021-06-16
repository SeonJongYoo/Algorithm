# 방 번호


# 값을 순서대로 체크하면 안됨!
n = list(map(int, input()))
st = [1]*10
cnt = 1
while True:
    if len(n) == 1:
        break
    for i in range(10):
        for j in range(len(n)):
            if st[i] == 0 and i == n[j]:
                if i == 9 and st[6] == 1:
                    st[6] = 0
                    n[j] = -1
                elif i == 6 and st[9] == 1:
                    st[9] = 0
                    n[j] = -1
                else:
                    break
            elif st[i] == 1 and i == n[j]:
                st[i] = 0
                n[j] = -1
    if sum(n) == -len(n):
        break
    else:
        cnt += 1
        st = [1]*10
print(cnt)