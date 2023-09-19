import sys
sys.stdin = open('1940_input.txt')

input = sys.stdin.readline

N = int(input())
M = int(input())

lst = list(map(int, input().split()))

lst.sort()

cnt = 0
s, e = 0, N-1

while s < e:
    if lst[s] + lst[e] == M:
        cnt += 1
        s += 1
        e -= 1
    elif lst[s] + lst[e] < M:
        s += 1
    else:
        e -= 1
print(cnt)
