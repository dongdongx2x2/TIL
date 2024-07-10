import sys
sys.stdin = open('9207_input.txt')

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(arr, pins, moves):
    global min_pins, min_moves

    if pins < min_pins or (pins == min_pins and moves < min_moves):
        min_pins = pins
        min_moves = moves

    for x in range(5):
        for y in range(9):
            if arr[x][y] == 'o':

                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    nnx, nny = nx + dx[i], ny + dy[i]

                    if 0 <= nx < 5 and 0 <= ny < 9 and 0 <= nnx < 5 and 0 <= nny < 9:
                        if arr[nx][ny] == 'o' and arr[nnx][nny] == '.':

                            arr[x][y] = '.'
                            arr[nx][ny] = '.'
                            arr[nnx][nny] = 'o'

                            dfs(arr, pins - 1, moves + 1)

                            arr[x][y] = 'o'
                            arr[nx][ny] = 'o'
                            arr[nnx][nny] = '.'



n = int(input())

for _ in range(n):
    arr = [list(input().rstrip()) for _ in range(5)]

    if _ < n - 1:
        input()

    pins = sum(row.count('o') for row in arr)
    min_pins = pins
    min_moves = 0

    dfs(arr, pins, 0)

    print(min_pins, min_moves)


