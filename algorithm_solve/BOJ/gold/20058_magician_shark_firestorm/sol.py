import sys
sys.stdin = open('20058_input.txt')

input = sys.stdin.readline

from collections import deque

def turn_and_melt(arr, L):

    new_arr = [[0] * (2 ** N) for _ in range(2 ** N)]

    for x in range(0, 2**N, 2**L):
        for y in range(0, 2**N, 2**L):
            for i in range(2**L):
                for j in range(2**L):
                    new_arr[x+j][y+2**L-i-1] = arr[x+i][y+j]

    arr = new_arr
    # print(arr)
    tem = []
    for i in range(2**N):
        for j in range(2**N):
            cnt = 0

            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ni, nj = i+di, j+dj
                if 0<=ni<2**N and 0<=nj<2**N and arr[ni][nj] != 0:
                    cnt += 1
            if cnt < 3 and arr[i][j] > 0:
                tem.append((i,j))
    # 한번에 뺴줘야함
    for i, j in tem:
        arr[i][j] -= 1


    return arr



N, Q = map(int, input().split())

arr = [list(map(int,input().split())) for _ in range(2**N)]
lst = list(map(int,input().split()))

for L in lst:
    arr = turn_and_melt(arr, L)

# 남아있는 합 구하기,

result = 0
for lst in arr:
    result += sum(lst)
print(result)

# 가장 큰 덩어리 구하기

v = [[0]*(2**N) for _ in range(2**N)]


mxmx = 0
for i in range(2**N):
    for j in range(2**N):
        if v[i][j] == 1 or arr[i][j] == 0:
            continue

        cnt = 0
        q = deque()
        q.append((i,j))
        v[i][j] = 1

        while q:
            ci, cj = q.popleft()
            cnt += 1

            for di, dj in ((1, 0), (-1,0), (0,1), (0,-1)):
                ni, nj = ci+di, cj+dj
                if 0 <= ni < 2**N and 0 <= nj < 2**N and v[ni][nj] == 0 and arr[ni][nj] != 0:
                    v[ni][nj] = 1
                    q.append((ni,nj))
        mxmx = max(cnt, mxmx)
print(mxmx)










