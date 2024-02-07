import sys
sys.stdin = open('16235_input.txt')

input = sys.stdin.readline

from collections import deque

def spring_summer():
    for i in range(n):
        for j in range(n):
            tem_len = len(tree_lst[i][j])
            for k in range(tem_len):
                if tree_lst[i][j][k] <= start_arr[i][j]:
                    start_arr[i][j] -= tree_lst[i][j][k]
                    tree_lst[i][j][k] += 1
                else:
                    for _ in range(k, tem_len):
                        start_arr[i][j] += tree_lst[i][j].pop() // 2
                    break


def fall():
    for i in range(n):
        for j in range(n):
            for k in tree_lst[i][j]:
                if k % 5 == 0:
                    for dx, dy in ((1, 0), (-1, 0), (1, 1), (-1, -1), (0, 1), (0, -1), (1, -1), (-1, 1)):
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < n and 0 <= ny < n:
                            tree_lst[nx][ny].appendleft(1)

def winter():
    for i in range(n):
        for j in range(n):
            start_arr[i][j] += arr[i][j]

n, m, k = map(int, input().split())
tree_lst = [[deque() for _ in range(n)] for _ in range(n)]
arr = [list(map(int, input().split())) for _ in range(n)]
start_arr = [[5] * n for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    tree_lst[x-1][y-1].append(z)

for _ in range(k):
    spring_summer()
    fall()
    winter()

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(tree_lst[i][j])
print(ans)
