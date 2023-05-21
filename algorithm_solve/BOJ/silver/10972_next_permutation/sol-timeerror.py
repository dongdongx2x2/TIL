import sys
sys.stdin = open('10972_input.txt')

input = sys.stdin.readline
from itertools import permutations


N = int(input())
lst = list(map(int,input().split()))

tem = []
for per in permutations(sorted(lst), N):
    tem.append(list(per))

for i in range(len(tem)):
    if tem[i] == lst:
        if i == len(tem)-1:
            print(-1)
        else:
            print(*tem[i+1])