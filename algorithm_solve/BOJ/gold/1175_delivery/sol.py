import sys
sys.stdin = open('1175_input.txt')

input = sys.stdin.readline

from collections import deque

def bfs():
    q = deque()
    q.append((start[0], start[1], -1, 0, False, False))
    v = set()

    while q:
        cx, cy, cur_dir, time, visited_c1, visited_c2 = q.popleft()

        if visited_c1 and visited_c2:
            return time

        for next_dir in range(4):
            if next_dir == cur_dir:
                continue

            nx, ny = cx + dx[next_dir], cy + dy[next_dir]

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] != "#":
                new_visited_c1, new_visited_c2 = visited_c1, visited_c2

                if (nx, ny) == gifts[0]:
                    new_visited_c1 = True
                elif (nx, ny) == gifts[1]:
                    new_visited_c2 = True

                if (nx, ny, next_dir, new_visited_c1, new_visited_c2) not in v:
                    v.add((nx, ny, next_dir, new_visited_c1, new_visited_c2))
                    q.append((nx, ny, next_dir, time + 1, new_visited_c1, new_visited_c2))
    return -1

n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]

start = (-1, -1)
gifts = []
for i in range(n):
    for j in range(m):
        if arr[i][j] == "S":
            start = (i,j)
        elif arr[i][j] == "C":
            gifts.append((i, j))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

print(bfs())