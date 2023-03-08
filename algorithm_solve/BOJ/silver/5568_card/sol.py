import sys
sys.stdin = open('5568_input.txt')

input = sys.stdin.readline

n = int(input())
k = int(input())

lst = []
for _ in range(n):
    lst.append(input().rstrip())

from itertools import permutations

lst2=[]
for i in permutations(lst, k):
    lst2.append(''.join(i))
print(len(set(lst2)))
