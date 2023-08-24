import sys
sys.stdin = open('10814_input.txt')

input = sys.stdin.readline

N = int(input())

lst = []
for _ in range(N):
    a, b = input().split()
    a = int(a)
    lst.append((a,b))
lst.sort(key=lambda x:x[0])

for i in lst:
    print(*i)