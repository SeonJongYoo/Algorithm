# 덱


import sys
n = int(sys.stdin.readline().rstrip())
deque = []
for _ in range(n):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == 'push_front':
        deque.insert(0, int(command[1]))
    elif command[0] == 'push_back':
        deque.append(int(command[1]))
    elif command[0] == 'pop_front':
        if deque:
            print(deque[0])
            deque = deque[1:]
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if deque:
            print(deque[len(deque)-1])
            deque = deque[:len(deque)-1]
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(deque))
    elif command[0] == 'empty':
        if not deque:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if deque:
            print(deque[len(deque)-1])
        else:
            print(-1)