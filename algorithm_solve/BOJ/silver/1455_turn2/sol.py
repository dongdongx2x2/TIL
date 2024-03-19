import sys
sys.stdin = open('1455_input.txt')

input = sys.stdin.readline

def flip(x, y):
    for i in range(x+1):
        for j in range(y+1):
            arr[i][j] = 1 - arr[i][j]

n, m = map(int, input().split())

arr = [list(map(int, input().rstrip())) for _ in range(n)]

cnt = 0
for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        if arr[i][j] == 1:
            flip(i,j)
            cnt += 1
print(cnt)