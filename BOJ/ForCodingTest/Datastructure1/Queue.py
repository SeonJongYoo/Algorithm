# 큐
import sys
n = int(sys.stdin.readline().rstrip())
queue = []
for _ in range(n):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == 'push':
        queue.append(int(command[1]))
    elif command[0] == 'pop':
        if queue:
            print(queue[0])
            queue = queue[1:]
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if queue:
            print(queue[len(queue)-1])
        else:
            print(-1)