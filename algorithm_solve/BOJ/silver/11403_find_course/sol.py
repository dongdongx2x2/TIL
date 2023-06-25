import sys
sys.stdin = open('11403_input.txt')

input = sys.stdin.readline

N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] or (arr[i][k] and arr[k][j]):
                arr[i][j] = 1
for i in arr:
    print(*i)