import sys
sys.stdin = open('12738_input.txt')

input = sys.stdin.readline

from bisect import bisect_left

# binary를 이용한 LIS 구하기
N = int(input())
lst = list(map(int,input().split()))

dp = [lst[0]]

for i in range(1, N):
    if lst[i] > dp[-1]:
        dp.append(lst[i])
    else:
        idx = bisect_left(dp, lst[i])
        dp[idx] = lst[i]
print(len(dp))
