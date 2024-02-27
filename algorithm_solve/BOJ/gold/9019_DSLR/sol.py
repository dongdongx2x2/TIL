import sys
sys.stdin = open('9019_input.txt')

input = sys.stdin.readline

from collections import deque

def bfs():

    q = deque()
    q.append((a, ""))
    v[a] = True

    while q:
        num, dslr = q.popleft()

        if num == b:
            return dslr

        d = num * 2 % 10000
        if not v[d]:
            v[d] = True
            q.append((d, dslr + "D"))

        s = (num - 1) % 10000
        if not v[s]:
            v[s] = True
            q.append((s, dslr + "S"))

        l = num // 1000 + (num % 1000) * 10
        if not v[l]:
            v[l] = True
            q.append((l, dslr + "L"))

        r = num // 10 + (num % 10) * 1000
        if not v[r]:
            v[r] = True
            q.append((r, dslr + "R"))

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    v = [False] * 10001
    print(bfs())