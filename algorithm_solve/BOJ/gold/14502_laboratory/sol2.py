import sys
sys.stdin = open('14502_input.txt')
from collections import deque
from itertools import permutations
import copy

input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# ✨ 준비 1
safe_zone = []
virus = []
res = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


# ✨ BFS
def bfs():
    global res
    cnt = len(safe_zone) - 3
    ch_virus = deque([])
    for x, y in virus:
        ch_virus.append((x, y))
    while ch_virus:
        xx, yy = ch_virus.popleft()
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]
            if 0 <= nx < N and 0 <= ny < M and ch_board[nx][ny] == 0:
                ch_board[nx][ny] = 2
                ch_virus.append((nx, ny))
                cnt -= 1
    res = max(res, cnt)


# ✨ 준비 2
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            safe_zone.append((i, j))
        elif board[i][j] == 2:
            virus.append((i, j))

# ✨ 조합
for comb in permutations(safe_zone, 3):
    ch_board = copy.deepcopy(board)
    for x, y in comb:
        ch_board[x][y] = 1
    bfs()
print(res)