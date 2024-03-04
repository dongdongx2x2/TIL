import sys
sys.stdin = open('17825_input.txt')

input = sys.stdin.readline

adj = [[1], [2], [3], [4], [5],
         [6, 21], [7], [8], [9], [10],
         [11, 25], [12], [13], [14], [15],
         [16, 27], [17], [18], [19], [20],
         [32], [22], [23], [24], [30],
         [26], [24], [28], [29], [24],
         [31], [20], [32]]

score = [0, 2, 4, 6, 8,
         10, 12, 14, 16, 18,
         20, 22, 24, 26, 28,
         30, 32, 34, 36, 38,
         40, 13, 16, 19, 25,
         22, 24, 28, 27, 26,
         30, 35, 0]

def dfs(n, sm):
    global ans

    if n == 10:
        ans = max(ans, sm)
        return

    for j in range(4):
        s = v[j]

        if len(adj[s]) == 2:
            c = adj[s][1]
        else:
            c = adj[s][0]

        for _ in range(1, lst[n]):
            c = adj[c][0]

        if c == 32 or c not in v:
            v[j] = c
            dfs(n+1, sm + score[c])
            v[j] = s

lst = list(map(int, input().split()))

v = [0,0,0,0]
ans = 0
dfs(0,0)
print(ans)