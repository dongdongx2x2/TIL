import sys
sys.stdin = open('10845_input.txt')

input = sys.stdin.readline

N = int(input())

from collections import deque
q = deque([])

for _ in range(N):
    a = input().rstrip()

    if a == 'pop':
        if q:
            b = q.popleft()
            print(b)
        else:
            print(-1)
    elif a == 'size':
        print(len(q))

    elif a == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif a == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif a == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
    else:
        q.append(a[5:])