import sys
sys.stdin = open('2910_input.txt')

input = sys.stdin.readline

from collections import Counter

N, C = map(int, input().split())
lst = list(map(int, input().split()))

count = Counter(lst)

lst = []
for key, value in count.items():
    lst.append((key,value))

lst.sort(key=lambda x : -x[1])
# print(lst)
for i, j in lst:
    for _ in range(j):
        print(i, end=' ')

