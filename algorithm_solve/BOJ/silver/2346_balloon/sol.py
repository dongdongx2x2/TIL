import sys
sys.stdin = open('2346_input.txt')

input = sys.stdin.readline

from collections import deque

n = int(input())
q = deque(enumerate(map(int, input().split())))

ans = []

while q:
    i, paper = q.popleft()
    ans.append(i + 1)

    if paper > 0:
        q.rotate(-paper + 1)
    elif paper < 0:
        q.rotate(-paper)

print(*ans)