import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

#1 2 3 4 5 6 7     3 6 2 7 5 1 4

N, K = map(int, input().split())

q = deque(range(1, N+1))

lst = []
i = 0
while q:
    a = q.popleft()
    if i % K == K-1:
        lst.append(a)
    else:
        q.append(a)
    i += 1

a = str(lst).replace('[', '<')
b = a.replace(']', '>')

print(b)

