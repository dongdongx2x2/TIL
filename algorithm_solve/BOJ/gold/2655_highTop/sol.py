import sys
sys.stdin = open('2655_input.txt')

input = sys.stdin.readline

n = int(input())
arr = [(0,0,0,0)]
for i in range(1, n+1):
    a, h, w = map(int, input().split())
    arr.append((i,a,h,w))

arr.sort(key=lambda x:x[3])

dp = [0] * (n+1)
for i in range(1, n+1):
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            dp[i] = max(dp[i], arr[i][2] + dp[j])

mx_height = max(dp)
index = n
result = []

while index != 0:
    if mx_height == dp[index]:
        result.append(arr[index][0])
        mx_height -= arr[index][2]
    index -= 1

result = result[::-1]
print(len(result))
for i in result:
    print(i)
