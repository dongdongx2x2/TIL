import sys
sys.stdin = open('14391_input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]

result = 0
# 0: 가로, 1: 세로
for s in range(1 << n * m):
    sum = 0
    for i in range(n):
        cur = 0
        for j in range(m):
            k = i * m + j
            if (s & (1 << k)) == 0:
                cur = cur * 10 + board[i][j]
            else:
                sum += cur
                cur = 0
        sum += cur
    for j in range(m):
        cur = 0
        for i in range(n):
            k = i * m + j
            if (s & (1 << k)) != 0:
                cur = cur * 10 + board[i][j]
            else:
                sum += cur
                cur = 0
        sum += cur
    result = max(result, sum)
print(result)
