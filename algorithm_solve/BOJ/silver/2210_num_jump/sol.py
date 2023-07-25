import sys
sys.stdin = open('2210_input.txt')

input = sys.stdin.readline

def dfs(x, y, lst):
    if len(lst) == 6:
        if lst not in ans:
            ans.append(lst)
        return

    for dx, dy in ((1, 0),(-1, 0),(0, 1),(0,-1)):
        nx, ny = x + dx, y + dy

        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, lst + [arr[nx][ny]])


arr =[list(map(int,input().split())) for _ in range(5)]

ans = []

for i in range(5):
    for j in range(5):
        dfs(i,j, [arr[i][j]])

print(len(ans))
