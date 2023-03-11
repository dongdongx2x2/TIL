import sys
sys.stdin = open('10866_input.txt')

input = sys.stdin.readline

from collections import deque

N = int(input())

dq = deque([])
for _ in range(N):
    a = input().rstrip()

    if a == 'pop_front':
        if dq:
            b = dq.popleft()
            print(b)
        else:
            print(-1)

    elif a == 'pop_back':
        if dq:
            b = dq.pop()
            print(b)
        else:
            print(-1)

    elif a == 'size':
        print(len(dq))

    elif a == 'empty':
        if dq:
            print(0)
        else:
            print(1)

    elif a == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)

    elif a == 'back':
        if dq:
            print(dq[-1])
        else:
            print(-1)

    elif a[:9] == 'push_back':
        dq.append(a[10:])

    else:
        dq.appendleft(a[11:])

