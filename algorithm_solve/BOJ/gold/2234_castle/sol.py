import sys
sys.stdin = open('2234_input.txt')

input = sys.stdin.readline

from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x,y))
    v[x][y] = room_num
    size = 1

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < m and 0 <= ny < n and not v[nx][ny]:
                if not arr[cx][cy] & (1 << i):
                    q.append((nx, ny))
                    v[nx][ny] = room_num
                    size += 1
    return size

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(m)]
v = [[0] * n for _ in range(m)]

# 서북동남
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

rooms = []
room_num = 0

for i in range(m):
    for j in range(n):
        if not v[i][j]:
            room_num += 1
            room_size = bfs(i,j)
            rooms.append(room_size)

max_room = max(rooms)

max_double_room = 0

for x in range(m):
    for y in range(n):
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if v[x][y] != v[nx][ny]:
                    max_double_room = max(max_double_room,  rooms[v[x][y]-1] + rooms[v[nx][ny]-1])

print(room_num)
print(max_room)
print(max_double_room)