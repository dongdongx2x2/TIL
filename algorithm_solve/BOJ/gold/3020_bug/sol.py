import sys
sys.stdin = open('3020_input.txt')

input = sys.stdin.readline

from bisect import bisect_left

N, H = map(int,input().split())

bottom = []
top = []
for i in range(N):
    if i % 2:
        top.append(int(input()))
    else:
        bottom.append(int(input()))

bottom.sort()
top.sort()

cnt = 0
mxmx = 200001

for i in range(1, H+1):
    bottom_ = bisect_left(bottom, i)
    top_ = bisect_left(top, H-i+1)

    tem = N-(bottom_ + top_)

    if tem < mxmx:
        mxmx = tem
        cnt = 1
    elif tem == mxmx:
        cnt += 1
print(mxmx, cnt)