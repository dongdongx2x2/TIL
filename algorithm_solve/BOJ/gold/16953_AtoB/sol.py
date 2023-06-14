import sys
sys.stdin = open('16953_input.txt')

input = sys.stdin.readline

a, b = map(int, input().split())

cnt = 0
while (b!=a):
    cnt += 1
    res = b
    if b % 10 == 1:
        b //= 10

    elif b % 2 == 0:
        b //= 2

    if res == b:
        print(-1)
        break
else:
    print(cnt+1)