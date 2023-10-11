import sys
sys.stdin = open('16928_input.txt')

input = sys.stdin.readline
from collections import deque

def bfs(n):
    q = deque()
    q.append(n)

    while q:
        cx = q.popleft()

        for i in range(1, 7):
            nx = cx + i

            if nx > 100:
                continue

            tem = lst[nx]

            if v[tem] == 0:
                q.append(tem)
                v[tem] = v[cx] + 1

                if tem == 100:
                    return v[100]


N, M = map(int, input().split())

v = [0] * 101
lst = [i for i in range(101)]

for _ in range(N + M):
    x, y = map(int, input().split())
    lst[x] = y

print(bfs(1))


