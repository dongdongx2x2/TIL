import sys
sys.stdin = open('22945_input.txt')

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

left = 0
right = n - 1
mxmx = 0

while left < right:
    tem = (right - left - 1) * min(lst[left], lst[right])
    mxmx = max(tem, mxmx)

    if lst[left] < lst[right]:
        left += 1
    else:
        right -= 1
print(mxmx)