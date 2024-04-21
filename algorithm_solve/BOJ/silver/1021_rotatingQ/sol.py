import sys
sys.stdin = open('1021_input.txt')

input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())

lst = deque([i for i in range(1, n+1)])
index = list(map(int, input().split()))

cnt = 0
for num in index:
    while True:
        if lst[0] == num:
            lst.popleft()
            break
        else:
            if lst.index(num) <= len(lst) // 2:
                lst.rotate(-1)
                cnt += 1
            else:
                lst.rotate(1)
                cnt += 1

print(cnt)
