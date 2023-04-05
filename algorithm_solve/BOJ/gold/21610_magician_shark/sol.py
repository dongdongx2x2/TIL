import sys
sys.stdin = open('21610_input.txt')

input = sys.stdin.readline


def move(dir, distance):

    cloud_zone = []
    for i in range(N):
        for j in range(N):
            if cloud[i][j] == 1:
                cloud_zone.append((i,j))
                cloud[i][j] = 0

    di = [0, -1, -1, -1, 0, 1, 1, 1]
    dj = [-1, -1, 0, 1, 1, 1, 0, -1]


    cloud_tem = []
    for ci, cj in cloud_zone:
        ni = ci + di[dir-1]*distance
        nj = cj + dj[dir-1]*distance

        ni = ni % N
        nj = nj % N

        cloud[ni][nj] = 1

        arr[ni][nj] += 1
        cloud_tem.append((ni,nj))
    # print(cloud_tem)

    for ni, nj in cloud_tem:
        for ddi, ddj in ((-1,-1), (1, 1), (-1,1), (1, -1)):  # 대각선 4방향 확인
            nni = ni + ddi
            nnj = nj + ddj

            if 0<= nni < N and 0 <= nnj < N and arr[nni][nnj] != 0:
                arr[ni][nj] += 1

    new_cloud = []
    for i in range(N):
        for j in range(N):
            if (i,j) not in cloud_tem and arr[i][j] >= 2:
                arr[i][j] -= 2
                new_cloud.append((i,j))

    for x,y in cloud_tem:
        cloud[x][y] = 0

    for x,y in new_cloud:
        cloud[x][y] = 1


N, M = map(int, input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

cloud = [[0] * N for _ in range(N)]

cloud[N-2][0] = 1
cloud[N-2][1] = 1
cloud[N-1][0] = 1
cloud[N-1][1] = 1

# print(cloud)

for _ in range(M):
    a, b = map(int, input().split())
    move(a,b)

sm = 0
for i in range(N):
    for j in range(N):
        sm += arr[i][j]
print(sm)

