import sys
sys.stdin = open('2228_input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())

include = [[0] + [-1e9] * m for _ in range(n+1)]
notinclude = [[0] + [-1e9] * m for _ in range(n+1)]

for i in range(1, n+1):
    num = int(input())
    for j in range(1, m+1):
        notinclude[i][j] = max(include[i-1][j], notinclude[i-1][j])
        include[i][j] = max(include[i-1][j], notinclude[i-1][j-1]) + num

print(max(include[n][m], notinclude[n][m]))