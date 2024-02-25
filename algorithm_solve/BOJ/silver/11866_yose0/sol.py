import sys
sys.stdin = open('11866_input.txt')

input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())

yose = []
q = deque()

for i in range(1, n + 1):
    q.append(i)

while q:
    for i in range(k - 1):
        q.append(q.popleft())
    yose.append(q.popleft())

print("<", end="")
print(", ".join(map(str, yose)), end="")
print(">")