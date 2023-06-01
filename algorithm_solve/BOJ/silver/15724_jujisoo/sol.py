import sys
sys.stdin = open('15724_input.txt')

input = sys.stdin.readline

N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

sm = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        sm[i][j] = sm[i-1][j] + sm[i][j-1] - sm[i-1][j-1] + arr[i-1][j-1]


K = int(input())

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    s = sm[x2][y2] - sm[x2][y1-1] - sm[x1-1][y2] + sm[x1-1][y1-1]
    print(s)

