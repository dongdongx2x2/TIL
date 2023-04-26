import sys
sys.stdin = open('14002_input.txt')

input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))

dp = [1] * N


for i in range(1, N):

    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j] + 1)
mx = max(dp)
print(mx)

tem = []

for i in range(N-1, -1, -1):
    if dp[i] == mx:
        tem.append(lst[i])
        mx -=1

print(*tem[::-1])
