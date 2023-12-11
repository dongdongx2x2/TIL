import sys
sys.stdin = open('12886_input.txt')

input = sys.stdin.readline

from collections import deque

def bfs():
    # global a, b, c

    q = deque()
    q.append((a, b))
    v[a][b] = 1

    while q:
        x, y = q.popleft()

        z = t - x - y

        if x == y == z:
            return 1

        for ca, cb in (x, y), (y, z), (x, z):
            if ca < cb:
                cb -= ca
                ca += ca
            elif ca > cb:
                ca -= cb
                cb += cb
            else:
                continue
            cc = t - ca - cb

            x = min(ca, cb, cc)
            y = max(ca, cb, cc)

            if not v[x][y]:
                q.append((x,y))
                v[x][y] = 1
    return 0


a, b, c = map(int, input().split())

t = a + b + c

v = [[0] * (t + 1) for _ in range(t + 1)]

if t % 3 != 0:
    print(0)

else:
    print(bfs())