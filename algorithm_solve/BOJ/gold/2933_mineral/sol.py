import sys
sys.stdin = open("2933_input.txt")

input = sys.stdin.readline

from collections import deque

def throw(y, turn):
    if turn % 2 == 1:
        for i in range(c-1, -1, -1):
            if arr[y][i] == 'x':
                arr[y][i] = '.'
                break
    else:
        for i in range(c):
            if arr[y][i] == 'x':
                arr[y][i] = '.'
                break
    return arr

def find_cluster(arr):
    v = [[0] * c for _ in range(r)]
    q = deque()

    for i in range(c):
        if arr[r-1][i] == 'x':
            q.append((r-1, i))

    while q:
        x, y = q.popleft()

        for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
            nx, ny = x + dx, y + dy

            if 0 <= nx < r and 0 <= ny < c and v[nx][ny] == 0 and arr[nx][ny] == 'x':
                v[nx][ny] = 1
                q.append((nx,ny))
    cluster = []
    for i in range(r-1, -1, -1):
        for j in range(c):
            if arr[i][j] == 'x' and v[i][j] == 0:
                cluster.append((i,j))
    if cluster:
        return cluster, True, v
    else:
        return cluster, False, v

def move(arr, cluster, v):
    down_min = int(1e9)

    for x, y in cluster:
        down_cnt = 0
        for i in range(x+1, r):
            if arr[i][y] == '.':
                down_cnt += 1
            if arr[i][y] == 'x' and v[i][y] == 1:
                break
        down_min = min(down_min, down_cnt)

    for x, y in cluster:
        arr[x][y] = '.'
        arr[x+down_min][y] = 'x'

    return arr

r, c = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(r)]
n = int(input())
commands = list(map(int, input().split()))

for i in range(n):
    arr = throw(r - commands[i], i)

    cluster, check, v = find_cluster(arr)

    if check:
        arr = move(arr, cluster, v)

for i in range(r):
    for j in range(c):
        print(arr[i][j], end = '')
    print()