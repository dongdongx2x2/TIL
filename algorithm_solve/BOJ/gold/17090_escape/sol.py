import sys
sys.stdin = open('17090_input.txt')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return 1

    if v[x][y] != -1:
        return v[x][y]

    v[x][y] = 0
    print(v)
    if arr[x][y] == "D":
        v[x][y] = dfs(x+1, y)
    elif arr[x][y] == "U":
        v[x][y] = dfs(x-1, y)
    elif arr[x][y] == "R":
        v[x][y] = dfs(x, y+1)
    elif arr[x][y] == "L":
        v[x][y] = dfs(x, y-1)

    return v[x][y]

n, m = map(int, input().split())

arr = [list(input().rstrip()) for _ in range(n)]
v = [[-1] * m for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j):
            ans += 1
print(ans)
