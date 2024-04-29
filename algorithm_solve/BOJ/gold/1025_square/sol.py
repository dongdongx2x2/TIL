import sys
sys.stdin = open('1025_input.txt')

input = sys.stdin.readline

def check(num):
    return int(num**0.5) ** 2 == num

n, m = map(int, input().split())
arr = [input().rstrip() for _ in range(n)]

mxmx = -1

for start_row in range(n):
    for start_col in range(m):

        for d_row in range(-n, n):
            for d_col in range(-m, m):

                if d_row == 0 and d_col == 0:
                    continue

                num = ''
                row, col = start_row, start_col

                while 0 <= row < n and 0 <= col < m:
                    num += arr[row][col]

                    if check(int(num)):
                        mxmx = max(mxmx, int(num))

                    row += d_row
                    col += d_col
print(mxmx)
