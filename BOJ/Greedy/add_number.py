while True:
    num = list(map(int, input().split()))
    N = num[0]
    if N == 0:
        break
    num.remove(N)
    num.sort()
    num_1 = ""; num_2 = ""
    if N % 2 == 0:
        tmp_1 = 0
        while num[tmp_1] == 0:
            tmp_1 += 1
        num_1 += str(num[tmp_1])
        num_2 += str(num[tmp_1+1])
        num.remove(num[tmp_1])
        num.remove(num[tmp_1])
        for i in range(len(num)):
            if i % 2 == 0:
                num_1 += str(num[i])
            else:
                num_2 += str(num[i])
    else: # N이 홀수인 경우
        tmp_2 = 0
        while num[tmp_2] == 0:
            tmp_2 += 1
        num_1 += str(num[tmp_2])
        num_2 += str(num[tmp_2+1])
        num.remove(num[tmp_2])
        num.remove(num[tmp_2])
        for i in range(len(num)):
            if i % 2 == 0:
                num_1 += str(num[i])
            else:
                num_2 += str(num[i])
    sum = int(num_1) + int(num_2)
    print(sum)
