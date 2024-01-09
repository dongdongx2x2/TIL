import sys
sys.stdin = open('2141_input.txt')

input = sys.stdin.readline

n = int(input())

lst = []
cnt = 0
for _ in range(n):
    x, a = map(int, input().split())
    lst.append((x,a))
    cnt += a

lst.sort()

num = 0
for i in range(n):
    num += lst[i][1]
    if num >= cnt / 2:
        print(lst[i][0])
        break