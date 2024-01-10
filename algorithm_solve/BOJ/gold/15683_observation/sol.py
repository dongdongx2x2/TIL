import sys
sys.stdin = open('15683_input.txt')

input = sys.stdin.readline

from copy import deepcopy

def check(arr, direction, x, y):
    for i in direction:
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                break

            if arr[nx][ny] == 6:
                break

            elif arr[nx][ny] == 0:
                arr[nx][ny] = -1

def dfs(depth, arr):
    global mimi

    if depth == len(cctv):
        cnt = 0
        for k in range(n):
            for w in range(m):
                if arr[k][w] == 0:
                    cnt += 1
        mimi = min(cnt, mimi)
        return

    tem = deepcopy(arr)
    cctv_n, x, y = cctv[depth]

    for i in dirs[cctv_n]:
        check(tem, i, x, y) # 채우기
        dfs(depth+1, tem)
        tem = deepcopy(arr) # 초기화


n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

cctv = []

for i in range(n):
    for j in range(m):
        if arr[i][j] not in [0,6]:
            cctv.append((arr[i][j], i, j))

dx = [-1,0,1,0]
dy = [0,1,0,-1]
dirs = {
    1: [[0], [1], [2], [3]],
    2: [[0,2], [1,3]],
    3: [[0,1], [1,2], [2,3],[0,3]],
    4: [[0,1,2], [0,1,3], [1,2,3], [0,2,3]],
    5: [[0,1,2,3]]
}

mimi = 1e9

dfs(0, arr)

print(mimi)


