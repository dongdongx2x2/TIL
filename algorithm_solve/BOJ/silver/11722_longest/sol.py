import sys
sys.stdin = open('11722_input.txt')

input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if lst[j] > lst[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))