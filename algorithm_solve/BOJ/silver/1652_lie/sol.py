import sys

sys.stdin = open('1652_input.txt')

input = sys.stdin.readline

n = int(input())
board = [list(input()) for _ in range(n)]

ans = [0, 0]
for i in range(n):
    r, c = 0, 0
    for j in range(n):
        if board[i][j] == '.':
            r += 1
        else:
            r = 0
        if r == 2:
            ans[0] += 1

        if board[j][i] == '.':
            c += 1
        else:
            c = 0
        if c == 2:
            ans[1] += 1
print(*ans)
