import sys
sys.stdin = open('2798_input.txt')

input = sys.stdin.readline

N, M = map(int, input().split())

card = list(map(int, input().split()))

from itertools import combinations

result = 0
for i in combinations(card, 3):
    if result <= sum(i) <= M:
        result = sum(i)
print(result)