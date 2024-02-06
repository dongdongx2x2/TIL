import sys
sys.stdin = open('5904_input.txt')

input = sys.stdin.readline

def moo(length, cur, N):
    left = (length - cur) // 2

    if N <= left:
        return moo(left, cur-1, N)
    elif N > left + cur:
        return moo(left, cur-1, N-left-cur)
    else:
        if N - left - 1:
            return "o"
        else:
            return "m"

N = int(input())

length, n = 3, 0
while N > length:
    n += 1
    length = length * 2 + n + 3

print(moo(length, n+3, N))