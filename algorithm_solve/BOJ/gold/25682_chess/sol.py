import sys
sys.stdin = open('25682_input.txt')

input = sys.stdin.readline

N, M, K = map(int, input().split())

def board(color):
    prefix = [[0] * (M + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(M):
            if (i + j) % 2 == 0:
                tem = arr[i][j] != color
            else:
                tem = arr[i][j] == color
            prefix[i + 1][j + 1] = prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j] + tem

    cnt = 99999999
    for i in range(1, N - K + 2):
        for j in range(1, M - K + 2):
            cnt = min(cnt, prefix[i + K - 1][j + K - 1] - prefix[i + K - 1][j - 1] - prefix[i - 1][j + K - 1] + prefix[i - 1][j - 1])
    return cnt

arr = [list(input().rstrip()) for _ in range(N)]

print(min(board("B"), board("W")))


