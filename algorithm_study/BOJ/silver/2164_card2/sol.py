import sys
sys.stdin = open('input.txt')

from collections import deque

N = int(input())

lst = deque(range(1,N+1))

while len(lst) != 1:
    lst.popleft()
    lst.append(lst.popleft())
print(*lst) # 시간복잡도를 해결하기 위해 deque사용