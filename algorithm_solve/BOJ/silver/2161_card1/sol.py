import sys
sys.stdin = open('2161_input.txt')

input = sys.stdin.readline

from collections import deque

N = int(input())

card = deque(i for i in range(1, N+1))
tem = []
while len(card) != 1:
    tem.append(card.popleft())
    card.append(card.popleft())

for i in tem:
    print(i, end=' ')
print(card[0])