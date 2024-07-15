import sys
sys.stdin = open('11687_input.txt')

input = sys.stdin.readline

def count_zero(n):
    cnt = 0
    while n > 0:
        n //= 5
        cnt += n
    return cnt

m = int(input())

left, right, = 0, 5 * m
result = -1

while left <= right:
    mid = (left + right) // 2

    if count_zero(mid) < m:
        left = mid + 1

    else:
        right = mid - 1
        if count_zero(mid) == m:
            result = mid

print(result)