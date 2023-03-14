import sys
sys.stdin = open('15654_input.txt')

input = sys.stdin.readline

N, M = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()
from itertools import permutations

for i in permutations(lst, M):
    print(*i)


