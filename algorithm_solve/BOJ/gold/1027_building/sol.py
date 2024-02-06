import sys
sys.stdin = open('1027_input.txt')

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

ans = [0] * n


for i in range(n):
    left, right = float('inf'), float('-inf')
    for j in range(i-1, -1, -1):
        slope = (lst[i] - lst[j]) / (i - j)
        if slope < left:
            left = slope
            ans[i] += 1

    for j in range(i+1, n):
        slope = (lst[i] - lst[j]) / (i - j)
        if slope > right:
            right = slope
            ans[i] += 1

print(max(ans))

