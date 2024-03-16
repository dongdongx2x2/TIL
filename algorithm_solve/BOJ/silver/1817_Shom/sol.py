import sys
sys.stdin = open('1817_input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())

if n == 0:
    print(0)

else:
    lst = list(map(int, input().split()))
    w = 0
    cnt = 1

    for i in lst:
        if i + w <= m:
            w += i

        else:
            w = i
            cnt += 1
    print(cnt)