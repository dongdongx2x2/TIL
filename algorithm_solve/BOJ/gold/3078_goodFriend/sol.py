import sys
sys.stdin = open('3078_input.txt')

input = sys.stdin.readline

from collections import deque

n, k = map(int, input().split())

dic = {}

cnt = 0

for i in range(n):
    name = input().rstrip()
    length = len(name)

    if length not in dic:
        dic[length] = deque()

    while dic[length] and i - dic[length][0] > k:
        dic[length].popleft()

    cnt += len(dic[length])

    dic[length].append(i)

print(cnt)

