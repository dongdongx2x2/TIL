import sys
sys.stdin = open('1449_input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())

lst = list(map(int, input().split()))
lst.sort()

s = lst[0]

cnt = 1

for i in lst[1:]:
    if i in range(s, s+m):
        continue
    else:
        s = i
        cnt += 1
print(cnt)