import sys
sys.stdin = open('15831_input.txt')

input = sys.stdin.readline

n, b, w = map(int, input().split())
lst = list(input().rstrip())

mxmx = 0
left = 0
w_cnt = 0
b_cnt = 0

for right in range(n):
    if lst[right] == "W":
        w_cnt += 1
    else:
        b_cnt += 1

    while b_cnt > b:
        if lst[left] == "W":
            w_cnt -= 1
        else:
            b_cnt -= 1
        left += 1

    if w_cnt >= w:
        mxmx = max(mxmx, right - left + 1)

print(mxmx)
