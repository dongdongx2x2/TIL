import sys
sys.stdin = open('25194_input.txt')

input = sys.stdin.readline

from itertools import combinations

def check():
    for r in range(1, n + 1):
        for comb in combinations(tem, r):
            if sum(comb) % 7 == 4:
                return "YES"

    return "NO"

n = int(input())
lst = list(map(int, input().split()))

tem = []
for i in lst:
    if i % 7 != 0:
        tem.append(i%7)

if len(tem) < 7:
    print(check())

else:
    print("YES")