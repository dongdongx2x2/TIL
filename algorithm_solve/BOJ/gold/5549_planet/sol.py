import sys
sys.stdin = open('5549_input.txt')

input = sys.stdin.readline

m, n = map(int, input().split())
k = int(input())
arr = [list(input().rstrip()) for _ in range(m)]

prefix_sum_J = [[0] * (n + 1) for _ in range(m + 1)]
prefix_sum_O = [[0] * (n + 1) for _ in range(m + 1)]
prefix_sum_I = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        prefix_sum_J[i][j] = prefix_sum_J[i-1][j] + prefix_sum_J[i][j-1] - prefix_sum_J[i-1][j-1] + (arr[i-1][j-1] == 'J')
        prefix_sum_O[i][j] = prefix_sum_O[i-1][j] + prefix_sum_O[i][j-1] - prefix_sum_O[i-1][j-1] + (arr[i-1][j-1] == 'O')
        prefix_sum_I[i][j] = prefix_sum_I[i-1][j] + prefix_sum_I[i][j-1] - prefix_sum_I[i-1][j-1] + (arr[i-1][j-1] == 'I')

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    J = prefix_sum_J[x2][y2] - prefix_sum_J[x2][y1 - 1] - prefix_sum_J[x1 - 1][y2] + prefix_sum_J[x1 - 1][y1 - 1]
    O = prefix_sum_O[x2][y2] - prefix_sum_O[x2][y1 - 1] - prefix_sum_O[x1 - 1][y2] + prefix_sum_O[x1 - 1][y1 - 1]
    I = prefix_sum_I[x2][y2] - prefix_sum_I[x2][y1 - 1] - prefix_sum_I[x1 - 1][y2] + prefix_sum_I[x1 - 1][y1 - 1]

    print(J, O, I)
