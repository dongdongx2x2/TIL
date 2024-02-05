import sys
sys.stdin = open('3151_input.txt')

input = sys.stdin.readline

from bisect import bisect_left

n = int(input())
lst = list(map(int, input().split()))

lst.sort()

cnt = 0
for i in range(n-2):
    left, right = i+1, n-1

    while left < right:
        tem = lst[i] + lst[left] + lst[right]

        if tem > 0:
            right -= 1

        elif tem < 0:
            left += 1

        else:
            if lst[left] == lst[right]:
                cnt += right - left

            else:
                idx = bisect_left(lst, lst[right])
                cnt += right - idx + 1

            left += 1

print(cnt)