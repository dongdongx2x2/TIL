import sys
sys.stdin = open('1038_input.txt')

input = sys.stdin.readline

from itertools import combinations

n = int(input())

ans = []

for i in range(1, 11):
    for j in combinations(range(10), i):
        tem = list(map(str, j[::-1]))
        tem = ''.join(tem)
        ans.append(int(tem))

ans.sort()
if n >= len(ans):
    print(-1)
else:
    print(ans[n])

