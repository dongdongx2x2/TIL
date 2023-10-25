import sys
sys.stdin = open("1525_input.txt")

input = sys.stdin.readline
from collections import deque

def bfs():
    v = {}
    v[start] = 0

    q = deque()
    q.append(start)

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while q:
        now = q.popleft()

        if now == goal:
            return v[goal]

        zero = now.find("0")

        x = zero // 3
        y = zero % 3

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 3 and 0 <= ny < 3:
                next = list(now)
                next_zero = nx * 3 + ny
                next[zero], next[next_zero] = next[next_zero], next[zero]
                next = "".join(next)

                if next not in v:
                    v[next] = v[now] + 1
                    q.append(next)
    return -1

start = ""
for _ in range(3):
    start += "".join(input().split())
goal = "123456780"
# print(start)
print(bfs())