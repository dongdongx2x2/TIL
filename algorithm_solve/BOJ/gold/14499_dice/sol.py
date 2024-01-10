import sys
sys.stdin = open('14499_input.txt')

input = sys.stdin.readline

def turn(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1: #동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c

    elif dir == 2: #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d

    elif dir == 3: #북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b

    else: # 남
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e


n, m, x, y, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

news = list(map(int, input().split()))

dx = [0,0,-1,1]
dy = [1,-1,0,0]
dice = [0] * 6

for dir in news:
    nx = x + dx[dir - 1]
    ny = y + dy[dir - 1]

    if 0 <= nx < n and 0 <= ny < m:
        turn(dir)
        if arr[nx][ny] == 0:
            arr[nx][ny] = dice[-1]

        else:
            dice[-1] = arr[nx][ny]
            arr[nx][ny] = 0

        print(dice[0])
        x, y = nx, ny

