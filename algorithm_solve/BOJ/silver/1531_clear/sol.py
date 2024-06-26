import sys
sys.stdin = open('1531_input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0] * 100 for _ in range(100)]

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1 - 1, x2):
        for j in range(y1 - 1, y2):
            arr[i - 1][j - 1] += 1

cnt = 0

for i in range(100):
    for j in range(100):
        if arr[i][j] > m:
            cnt += 1
print(cnt)
