import sys
sys.stdin = open('21757_input.txt')

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

prefix_sum = [0] * (n+1)

for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i-1] + lst[i-1]

total_sum = prefix_sum[n]

if total_sum % 4 != 0:
    print(0)
else:
    target = total_sum // 4
    first_count = 0
    second_count = 0
    third_count = 0

    for i in range(1, n):
        if prefix_sum[i] == 3 * target:
            third_count += second_count
        if prefix_sum[i] == 2 * target:
            second_count += first_count
        if prefix_sum[i] == target:
            first_count += 1

    print(third_count)
