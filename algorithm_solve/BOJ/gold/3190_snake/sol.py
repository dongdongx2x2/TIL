import sys
sys.stdin = open('3190_input.txt')
input = sys.stdin.readline
from collections import deque

def turn(dir, c):
    if c == 'D':
        dir = (dir + 1) % 4
    else:
        dir = (dir - 1) % 4

    return dir


N = int(input())
K = int(input())
arr = [[0] * N for _ in range(N)]

for _ in range(K):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1

L = int(input())

L_lst = []
for _ in range(L):
    x, c = input().split()
    L_lst.append((int(x), c))

dx = [0,1,0,-1]# 동남서북
dy = [1,0,-1,0]


(x, y) = (0,0)
arr[x][y] = 2

dir = time = num = 0

q = deque()
q.append((x,y))

while True:
    nx = x + dx[dir]
    ny = y + dy[dir]

    if 0<=nx< N and 0<=ny<N and arr[nx][ny] != 2:
        if arr[nx][ny] == 0:
            arr[nx][ny] = 2
            q.append((nx,ny))
            px, py = q.popleft()
            arr[px][py] = 0

        elif arr[nx][ny] == 1:
            arr[nx][ny] = 2
            q.append((nx,ny))
    else:
        time += 1
        break

    x, y = nx, ny
    time += 1
    if num < L and time == L_lst[num][0]:
        dir = turn(dir, L_lst[num][1])
        num += 1

print(time)