import sys
sys.stdin = open('15665_input.txt')

input = sys.stdin.readline

def dfs(n, tlst):

    if n == M:
        ans.append(tlst)
        return

    prev = 0
    for j in range(N):
        if prev != lst[j]:
            prev = lst[j]
            dfs(n+1,tlst + [lst[j]])




N, M = map(int, input().split())

lst = sorted(list(map(int, input().split())))

v = [0] * (N+1)

ans = []

dfs(0,[])

for i in ans:
    print(*i)