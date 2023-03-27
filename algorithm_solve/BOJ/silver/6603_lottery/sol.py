import sys
sys.stdin = open('6603_input.txt')

input = sys.stdin.readline

def dfs(n,s,tlst):

    if n == 6:
        ans.append(tlst)
        return

    for j in range(s, N):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, j, tlst + [lst[j]])
            v[j] = 0

while True:
    lst = list(map(int,input().split()))
    if lst[0] == 0:
        break

    N = lst.pop(0)

    v = [0] * N
    ans = []
    dfs(0, 0, [])

    for i in ans:
        print(*i)
    print()