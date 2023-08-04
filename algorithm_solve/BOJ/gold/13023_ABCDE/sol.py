import sys
sys.stdin = open('13023_input.txt')

input = sys.stdin.readline

def dfs(n, depth):
    global ans
    if depth == 5:
        ans = 1
        return

    for j in arr[n]:
        if v[j] == 0:
            v[j] = 1
            dfs(j, depth +1)
            v[j] = 0


N, M = map(int, input().split())

arr = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

ans = 0
for i in range(N):
    v = [0] * N
    v[i] = 1
    dfs(i, 1)
    if ans:
        break
print(ans)
