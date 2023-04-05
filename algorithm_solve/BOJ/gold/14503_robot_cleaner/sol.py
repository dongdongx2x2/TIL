import sys
sys.stdin = open('14503_input.txt')

input = sys.stdin.readline


dx = [-1,0,1,0]
dy = [0,1,0,-1]

def robot(x,y,d):


    while True:
        arr[x][y] = 2


        flag = True
        while flag:

            for i in ((d-1)%4, (d-2)%4,(d-3)%4,d):
                nx, ny = x + dx[i], y + dy[i]
                if arr[nx][ny] == 0:
                    x,y,d = nx,ny,i
                    flag = False
                    break
            else:
                if arr[x - dx[d]][y- dy[d]] == 1:
                    return
                else:
                    x,y = x-dx[d], y-dy[d]

N, M = map(int,input().split())

r,c,d = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
# print(arr)
robot(r,c,d)

# print(arr)
sm = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            sm += 1

print(sm)