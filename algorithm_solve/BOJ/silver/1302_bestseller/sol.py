import sys
sys.stdin = open('1302_input.txt')

input = sys.stdin.readline

from collections import Counter

N = int(input())

lst = []

for _ in range(N):
    lst.append(input().rstrip())

tem = Counter(lst)

mxmx = max(tem.values())

tem2 = []
for i in tem.keys():
    if tem[i] == mxmx:
        tem2.append(i)
tem2.sort()

print(tem2[0])