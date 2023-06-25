import sys
sys.stdin = open('2251_input.txt')

input = sys.stdin.readline

from collections import deque

def water(x,y):
    if v[x][y] == 0:
        v[x][y] = 1
        q.append((x,y))

def bfs():

    while q:
        x, y = q.popleft()
        z = C - x - y

        if x == 0:
            result.append(z)

        w = min(x, B-y)
        water(x - w, y + w)

        w = min(x, C-z)
        water(x - w, y)

        w = min(y, A-x)
        water(x + w, y - w)

        w = min(y, C-z)
        water(x, y - w)

        w = min(z, A-x)
        water(x + w, y)

        w = min(z, B - y)
        water(x, y + w)


A, B, C = map(int,input().split())

v = [[0] * 201 for _ in range(201)]
v[0][0] = 1

q = deque()
q.append((0,0))

result = []
bfs()

print(*sorted(result))

