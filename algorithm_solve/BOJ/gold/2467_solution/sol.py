import sys
sys.stdin = open('2467_input.txt')

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

left, right = 0, n-1
ans = [lst[left], lst[right]]
mi = abs(lst[left] + lst[right])

while left < right:
    if abs(lst[left] + lst[right]) < mi:
        mi = abs(lst[left] + lst[right])
        ans = [lst[left], lst[right]]

    if lst[left] + lst[right] < 0:
        left += 1

    elif lst[left] + lst[right] > 0:
        right -= 1

    else:
        break

ans.sort()
print(*ans)