import sys
sys.stdin = open('1059_input.txt')

input = sys.stdin.readline

L = int(input())
S = list(map(int,input().split()))
n = int(input())

S.sort()


if n in S:
    print(0)

else:
    mimi = 0
    mxmx = 0
    for i in S:
        if i < n:
            mimi = i
        elif i > n and mxmx == 0:
            mxmx = i

    mxmx -= 1
    mimi += 1

    print((n-mimi) * (mxmx - n + 1) + (mxmx-n))
