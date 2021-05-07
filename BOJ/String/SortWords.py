# 단어 정렬

# 내가 작성한 코드
# 시간 초과 발생 - 선택 정렬 사용 -> 시간 복잡도: O(n^2)
'''n = int(input())
words = []
for _ in range(n):
    t = input()
    if t in words:
        continue
    words.append(t)
L = len(words)
Min_L = 0
# 선택 정렬 사용
for i in range(L-1):
    Min_L = i
    for j in range(i+1, L):
        if len(words[j]) < len(words[Min_L]):
            Min_L = j
        elif len(words[j]) == len(words[Min_L]):
            for k in range(len(words[Min_L])):
                if ord(words[j][k]) < ord(words[Min_L][k]):
                    Min_L = j
                    break
    if i != Min_L:
        tmp = words[Min_L]
        words[Min_L] = words[i]
        words[i] = tmp
for x in words:
    print(x)'''

# 내가 작성한 코드2 - 시간 초과 발생 - 시간 복잡도: O(n^2)
'''n = int(input())
words = []
for _ in range(n):
    t = input()
    if t in words:
        continue
    words.append(t)
L = len(words)
words.sort()
words_len = [len(words[i]) for i in range(L)]
words_len.sort()
for i in range(L):
    for j in range(i+1, L):
        if words_len[i] == len(words[j]):
            tmp = words[j]
            words[j] = words[i]
            words[i] = tmp
            break
for x in words:
    print(x)'''

# 내가 작성한 코드3 - Merge Sort(병합 정렬)사용 - O(nlogn)
n = int(input())
words = []
for _ in range(n):
    t = input()
    if t in words:
        continue
    words.append(t)


# *************************
def MergeSort(List): # 리스트 분리
    if len(List) <= 1:
        return List
    mid = len(List)//2
    leftList = List[:mid]
    rightList = List[mid:]
    leftList = MergeSort(leftList)
    rightList = MergeSort(rightList)
    res = Merge(leftList, rightList)
    return res


def Merge(left, right): # 리스트 병합
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if len(left[0]) < len(right[0]):
                result.append(left[0])
                left = left[1:]
            elif len(left[0]) > len(right[0]):
                result.append(right[0])
                right = right[1:]
            else:
                if left[0] < right[0]:
                    result.append(left[0])
                    left = left[1:]
                else:
                    result.append(right[0])
                    right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result
# ****************************
answer = MergeSort(words)
for x in answer:
    print(x)















