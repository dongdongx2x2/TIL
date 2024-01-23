import sys
sys.stdin = open('2665_input.txt')

input = sys.stdin.readline

from collections import deque

def bfs():
    q = deque()
    q.append((0,0))

    v[0][0] = 0

    while q:
        cx, cy = q.popleft()

        if (cx, cy) == (n-1, n-1):
            return v[cx][cy]

        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < n and 0 <= ny < n and v[nx][ny] == -1:
                if arr[nx][ny] == 1:
                    q.appendleft((nx, ny))
                    v[nx][ny] = v[cx][cy]

                else:
                    q.append((nx, ny))
                    v[nx][ny] = v[cx][cy] + 1

n = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(n)]

v = [[-1] * n for _ in range(n)]

print(bfs())
