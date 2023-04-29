import sys
sys.stdin = open('16935_input.txt')

input = sys.stdin.readline

def solve1(arr1):
    global arr
    tem_arr = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            tem_arr[i][j] = arr1[N-i-1][j]
    arr = tem_arr

def solve2(arr1):
    global arr
    tem_arr = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            tem_arr[i][j] = arr1[i][M-j-1]
    arr = tem_arr

def solve3(arr1):
    global arr
    tem_arr = [[0] * N for _ in range(M)]

    for i in range(M):
        for j in range(N):
            tem_arr[i][j] = arr1[N-j-1][i] #0,0 N,0/ 0,1 N-1,0/---
    arr = tem_arr

def solve4(arr1):
    global arr
    tem_arr = [[0] * N for _ in range(M)]

    for i in range(M):
        for j in range(N):
            tem_arr[i][j] = arr1[j][M-i-1] # 0,0 0,M/ 0,1 1,M/
                                           # 1,0 1,N-1/
    arr = tem_arr

def solve5(arr1):
    global arr
    tem_arr = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if i < N//2 and j < M//2: # 1사분면은 3사분면에서 떙겨오기
                tem_arr[i][j] = arr1[i-N//2][j]

            elif i < N//2 and j >= M//2: # 2사분면은 1사분면에서 떙겨오기기
                tem_arr[i][j] = arr1[i][j-M//2]

            elif i >= N//2 and j < M//2: # 4번은 3번에서 댕겨오기
                tem_arr[i][j] = arr1[i][j-M//2]

            elif i >= N//2 and j >= M//2:  # 3은 2번에서 떙겨오기
                tem_arr[i][j] = arr1[i-N//2][j]
    arr = tem_arr

def solve6(arr1):
    global arr
    tem_arr = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if i < N//2 and j < M//2: # 1번자리는 2번에서 떙겨오기
                tem_arr[i][j] = arr1[i][j-M//2]

            elif i < N//2 and j >= M//2: # 2번자리는은 3번자리에서 떙겨오기기
                tem_arr[i][j] = arr1[i-N//2][j]

            elif i >= N//2 and j < M//2: # 4번은 1번에서 댕겨오기
                tem_arr[i][j] = arr1[i-N//2][j]

            elif i >= N//2 and j >= M//2:  # 3은 4번에서 떙겨오기
                tem_arr[i][j] = arr1[i][j-M//2]
    arr = tem_arr



N, M, R = map(int,input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

numbers = list(map(int,input().split()))



for num in numbers:
    if num == 1:
        solve1(arr)
    elif num == 2:
        solve2(arr)
    elif num == 3:
        solve3(arr)
        N,M = M,N
    elif num == 4:
        solve4(arr)
        N, M = M, N
    elif num == 5:
        solve5(arr)
    elif num == 6:
        solve6(arr)

for lst in arr:
    print(*lst)