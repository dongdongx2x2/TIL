import sys
sys.stdin = open('10157_input.txt')

input = sys.stdin.readline


def check(arr):
    for i in range(y):
        for j in range(x):
            if arr[i][j] == N:
                return [j + 1, y - i]
    return [0]


x, y = map(int, input().split())
N = int(input())

arr =[[0] * x for _ in range(y)]
# print(arr)
    # 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = 2
arr[y-1][0] = 1
# print(arr)
cx, cy = y-1, 0
i = 0
while n <= x*y:
    nx = cx + dx[i]
    ny = cy + dy[i]
    if 0 <= nx < y and 0 <= ny <x and arr[nx][ny] == 0:
        arr[nx][ny] = n
        n += 1
        cx, cy = nx, ny
    else:
        i += 1
        if i == 4:
            i = 0
print(*check(arr))





