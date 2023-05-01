import sys
sys.stdin = open('16918_input.txt')

input = sys.stdin.readline

R, C, N = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(R)]


# 1초뒤 완전 0 2초뒤 리벌스 3초뒤 완전0 4초뒤 처음 5초뒤 0

tem = set()
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'O':
            tem.add((i,j))
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj = i+di, j+dj
                if 0<=ni< R and 0<= nj < C:
                    tem.add((ni,nj))

arr2 = [['O'] * C for _ in range(R)]
arr3 = [['O'] * C for _ in range(R)]
for i, j in tem:
    arr3[i][j] = '.'

tem2 = set()
for i in range(R):
    for j in range(C):
        if arr3[i][j] == 'O':
            tem2.add((i,j))
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ni,nj = i+di, j+dj
                if 0<=ni< R and 0<= nj < C:
                    tem2.add((ni,nj))

arr4 = [['O'] * C for _ in range(R)]
for i,j in tem2:
    arr4[i][j] = '.'



if N == 1:
    for lst in arr:
        print(''.join(lst))
elif N % 2 == 0:
    # print(arr2)
    for lst in arr2:
        print(''.join(lst))
elif N % 4 == 3:
    for lst in arr3:
        print(''.join(lst))
elif N % 4 == 1:
    for lst in arr4:
        print(''.join(lst))



