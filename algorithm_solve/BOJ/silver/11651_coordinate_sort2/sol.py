import sys
sys.stdin = open('11651_input.txt')

input = sys.stdin.readline

N = int(input())

lst = []
for _ in range(N):
    a, b = map(int,input().split())
    lst.append((a,b))

lst.sort(key=lambda x : (x[1], x[0]))

for i in lst:
    print(i[0], i[1])