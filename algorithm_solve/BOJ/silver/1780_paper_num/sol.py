import sys
sys.stdin = open('1780_input.txt')

input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]


result = [0, 0, 0]

def search(x, y, N):

    for i in range(x, x+N):
        for j in range(y, y+N):
            if arr[x][y] != arr[i][j]:
                for a in range(3):
                    for b in range(3):
                        search(x+a*N//3, y+b*N//3, N//3)
                return


    if arr[x][y] == -1:
        result[0] += 1
    elif arr[x][y] == 0:
        result[1] += 1
    elif arr[x][y] == 1:
        result[2] += 1


search(0, 0, N)

for i in result:
    print(i)
