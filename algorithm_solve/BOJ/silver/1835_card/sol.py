import sys
sys.stdin = open('1835_input.txt')

input = sys.stdin.readline

from collections import deque

n = int(input())
q = deque()
q.append(n)

for i in range(n-1, 0, -1):
    q.appendleft(i)
    for j in range(i):
        q.appendleft(q.pop())

print(*q)