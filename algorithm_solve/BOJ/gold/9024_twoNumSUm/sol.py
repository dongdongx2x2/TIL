import sys
sys.stdin = open('9024_input.txt')

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))

    lst.sort()

    l, r = 0, n - 1
    mxmx = int(1e9)
    cnt = 0

    while l < r:
        cur_sum = lst[l] + lst[r]
        cur_diff = abs(cur_sum - k)

        if cur_diff < mxmx:
            mxmx = cur_diff
            cnt = 1
        elif cur_diff == mxmx:
            cnt += 1

        if cur_sum < k:
            l += 1
        else:
            r -= 1
    print(cnt)
