import sys
sys.stdin = open('16395_input.txt')

input = sys.stdin.readline

n, k = map(int, input().split())
ans = [[] for _ in range(n)]

for i in range(0, n):
    for j in range(0, i + 1):
        if i == 0 or j == 0 or j == i:
            ans[i].append(1)
        else:
            ans[i].append(ans[i - 1][j - 1] + ans[i - 1][j])

print(ans[n - 1][k - 1])
