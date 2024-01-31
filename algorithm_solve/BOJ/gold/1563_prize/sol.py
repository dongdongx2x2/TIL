import sys
sys.stdin = open('1563_input.txt')

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
def dfs(day, late, no):
    if late >= 2 or no >= 3:
        return 0
    if day == n:
        return 1

    if dp[day][late][no] == -1:
        dp[day][late][no] = (dfs(day + 1, late, 0) + dfs(day + 1, late + 1, 0) + dfs(day + 1, late, no + 1))

    return dp[day][late][no]



n = int(input())
dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]
# print(dp)
print(dfs(0,0,0) % 1000000)
