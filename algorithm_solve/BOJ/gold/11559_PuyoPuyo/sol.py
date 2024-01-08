import sys
sys.stdin = open('11559_input.txt')

input = sys.stdin.readline

from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x,y))

    tem.append((x,y))

    v[x][y] = 1

    while q:
        cx, cy = q.popleft()

        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx,ny = cx + dx, cy+dy
            if 0 <= nx < 12 and 0 <= ny < 6 and arr[nx][ny] == arr[x][y] and v[nx][ny] == 0:
                q.append((nx,ny))
                tem.append((nx,ny))
                v[nx][ny] = 1

def delete(tem):
    for x, y in tem:
        arr[x][y] = '.'

def down(arr):

    new_arr = [['.' for _ in range(6)] for _ in range(12)]

    for i in range(6):
        tem = []

        for j in range(12):
            if arr[j][i] != '.':
                tem.append(arr[j][i])

        for j in range(11, -1, -1):
            if tem:
                new_arr[j][i] = tem.pop()
            else:
                break

    return new_arr

arr = [list(input().rstrip()) for _ in range(12)]

ans = 0
while True:
    flag = 0
    v = [[0] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if arr[i][j] != '.' and v[i][j] == 0:

                tem = []
                bfs(i,j)

                if len(tem) >= 4:
                    flag = 1
                    delete(tem)

    if flag == 0:
        break

    arr = down(arr)
    ans += 1

print(ans)

