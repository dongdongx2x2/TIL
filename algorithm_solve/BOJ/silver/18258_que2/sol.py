import sys

sys.stdin = open('18258_input.txt')

input = sys.stdin.readline

from collections import deque

n = int(input())
q = deque([])

for _ in range(n):
    a = input().split()
    if a[0] == 'push':
        q.append(a[1])
    elif a[0] == 'pop':
        if len(q):
            print(q.popleft())
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(q))
    elif a[0] == 'empty':
        if len(q):
            print(0)
        else:
            print(1)
    elif a[0] == 'front':
        if len(q):
            print(q[0])
        else:
            print(-1)
    elif a[0] == 'back':
        if len(q):
            print(q[-1])
        else:
            print(-1)
