import sys
sys.stdin = open('15685_input.txt')

input = sys.stdin.readline

n = int(input())

arr = [[0] * 101 for _ in range(101)]

di, dj = [0, -1, 0, 1], [1, 0, -1, 0]

for _ in range(n):
    sj, si, dr, g = map(int, input().split())

    lst = [(si, sj)]
    lst.append((si + di[dr], sj + dj[dr]))

    for _ in range(g):
        ei, ej = lst[-1]

        for i in range(len(lst) - 2, -1, -1):
            ci, cj = lst[i]
            lst.append((ei-(ej-cj), ej+(ei-ci)))

    for i in lst:
        arr[i[0]][i[1]] = 1

ans = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == arr[i][j+1] == arr[i+1][j] == arr[i+1][j+1] == 1:
            ans += 1
print(ans)