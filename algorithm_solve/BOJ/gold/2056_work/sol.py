import sys
sys.stdin = open('2056_input.txt')

input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)

for i in range(1, n + 1):
    lst = list(map(int, input().split()))

    if lst[1] == 0:
        dp[i] = lst[0]

    else:
        tem = []
        for j in lst[2:]:
            tem.append(dp[j])
        mx = max(tem)
        dp[i] = mx + lst[0]
# print(dp)
print(max(dp))
