import sys
sys.stdin = open('10163_input.txt')

input = sys.stdin.readline
N = int(input())

arr = [[0]*1002 for _ in range(1002)]
for n in range(1, N+1):
    si, sj, di, dj = map(int, input().split())
    for i in range(si, si + di):
        for j in range(sj, sj + dj):
            arr[i][j] = n

for n in range(1, N+1):
    cnt = 0
    for i in range(1002):
        for j in range(1002):
            if arr[i][j] == n:
                cnt += 1
    print(cnt)




