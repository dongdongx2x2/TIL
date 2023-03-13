import sys
sys.stdin = open('1182_input.txt')

input = sys.stdin.readline

N, S = map(int, input().split())

lst = list(map(int, input().split()))


from itertools import combinations

cnt = 0
for j in range(1, N+1):
    for i in combinations(lst, j):
        if sum(i) == S:
            cnt += 1
print(cnt)