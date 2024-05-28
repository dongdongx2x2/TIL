import sys
sys.stdin = open('2412_input.txt')

input = sys.stdin.readline

from collections import deque

def bfs():
    v = set()
    q = deque()
    q.append((0,0,0))
    while q:
        cx, cy, cnt = q.popleft()
        if cy == t:
            return cnt

        for i in range(-2, 3):
            for j in range(-2, 3):
                nx, ny = cx + i, cy + j

                if (nx, ny) in dots:
                    q.append((nx, ny, cnt + 1))
                    dots.remove((nx, ny))

    return -1


n, t = map(int, input().split())
dots = set()
for _ in range(n):
    x, y = map(int, input().split())
    dots.add((x,y))

print(bfs())