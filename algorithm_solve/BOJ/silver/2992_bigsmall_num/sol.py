import sys
sys.stdin = open('2992_input.txt')

input = sys.stdin.readline
from itertools import permutations

n = input().rstrip()
lst = []
for i in permutations(n):
    lst.append(''.join(i))
lst.sort(reverse=True)

i = lst.index(n)
# print(i)
print(lst[i-1] if i else 0)