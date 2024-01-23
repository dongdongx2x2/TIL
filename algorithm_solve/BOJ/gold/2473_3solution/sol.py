import sys
sys.stdin = open('2473_input.txt')

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

lst.sort()

mi = abs(lst[0] + lst[-1] + lst[n//2])

ans = [lst[0], lst[-1], lst[n//2]]

for i in range(n-2):
    left, right = i+1, n-1

    while left < right:
        tem = lst[i] + lst[left] + lst[right]

        if abs(tem) < mi:
            mi = abs(tem)
            ans = [lst[i], lst[left], lst[right]]

        if tem < 0:
            left += 1
        elif tem > 0:
            right -= 1
        else:
            break

ans.sort()
print(*ans)