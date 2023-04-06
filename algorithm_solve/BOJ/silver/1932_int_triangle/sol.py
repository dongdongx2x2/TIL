import sys
sys.stdin = open('1932_input.txt')
input = sys.stdin.readline

n = int(input())

arr = [[]]+[list(map(int,input().split())) for _ in range(n)]


for i in range(2, n+1):
    for j in range(i):

        if j == 0:
            left = 0
        else:
            left = arr[i-1][j-1]

        if j == i-1:
            up = 0

        else:
            up = arr[i-1][j]

        arr[i][j] = arr[i][j] + max(left,up)
print(max(arr[n]))



