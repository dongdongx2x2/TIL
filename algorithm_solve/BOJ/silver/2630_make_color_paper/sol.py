import sys
sys.stdin = open('2630_input.txt')

input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split()))for _ in range(N)]
result = [0, 0]
def search(x, y, N):

    for i in range(x, x+N):
        for j in range(y, y+N):
            if arr[x][y] != arr[i][j]:

                for a in range(2):
                    for b in range(2):
                        search(x+a*N//2, y+b*N//2, N//2)
                return

    if arr[x][y] == 0:
        result[0] += 1
    else:
        result[1] += 1

search(0, 0, N)

for i in result:
    print(i)