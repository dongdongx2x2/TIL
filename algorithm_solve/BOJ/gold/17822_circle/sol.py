import sys
sys.stdin = open('17822_input.txt')

input = sys.stdin.readline

from collections import deque

def check(arr):

    for i in range(1, n+1):
        for j in range(m):
            prev_j = (j-1+m) % m
            next_j = (j+1) % m
            if arr[i][j] == arr[i][prev_j] != 0:
                sset.add((i,j))
                sset.add((i,prev_j))

            if arr[i][j] == arr[i][next_j] != 0:
                sset.add((i,j))
                sset.add((i,next_j))

            if arr[i][j] == arr[i-1][j] != 0:
                sset.add((i,j))
                sset.add((i-1,j))

            if arr[i][j] == arr[i+1][j] != 0:
                sset.add((i,j))
                sset.add((i+1,j))

n, m, t = map(int, input().split())

lst = [[-1] * m]+ [deque(map(int, input().split())) for _ in range(n)] + [[-1] * m]


for _ in range(t):
    x, d, k = map(int, input().split())

    for i in range(1, n+1):
        if i % x == 0:
            if d == 0:
                lst[i].rotate(k)
            else:
                lst[i].rotate(-k)

    sset = set()

    check(lst)

    if sset:
        for x, y in sset:
            lst[x][y] = 0

    else:
        sm = 0
        cnt = 0
        for i in range(1, n+1):
            for j in range(m):
                if lst[i][j] != 0:
                    sm += lst[i][j]
                    cnt += 1
        if cnt == 0:
            aver = 0

        else:
            aver = sm / cnt

        for i in range(1, n+1):
            for j in range(m):
                if lst[i][j] != 0 and lst[i][j] < aver:
                    lst[i][j] += 1

                elif lst[i][j] != 0 and lst[i][j] > aver:
                    lst[i][j] -= 1


ans = 0
for i in range(1, n+1):
    ans += sum(lst[i])
print(ans)