import sys
sys.stdin = open('10942_input.txt')

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
m = int(input())

dp = [[0] * n for _ in range(n)]

for num_len in range(n):
    for a in range(n-num_len):
        b = a + num_len

        if a == b:
            dp[a][b] = 1

        elif lst[a] == lst[b]:
            if a + 1 == b:
                dp[a][b] = 1

            elif dp[a+1][b-1] == 1:
                dp[a][b] = 1


for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])