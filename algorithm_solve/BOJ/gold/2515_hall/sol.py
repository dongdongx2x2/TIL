import sys
sys.stdin = open('2515_input.txt')

input = sys.stdin.readline

n, s = map(int, input().split())

pictures = []
for _ in range(n):
    h, c = map(int, input().split())
    pictures.append((h, c))

pictures.sort()

dp = [0] * (n + 1)

def binary_search(target):
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if pictures[mid][0] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

for i in range(1, n + 1):
    h, c = pictures[i - 1]
    dp[i] = dp[i - 1]

    j = binary_search(h - s + 1)
    dp[i] = max(dp[i], dp[j] + c)

print(dp[n])