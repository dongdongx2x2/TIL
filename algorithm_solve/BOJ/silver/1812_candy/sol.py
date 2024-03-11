import sys
sys.stdin = open('1812_input.txt')

input = sys.stdin.readline

n = int(input())
s = 0
lst = []

for i in range(n):
    lst.append(int(input()))
    s += lst[i] * (-1)**i
a = s // 2

print(a)
for i in range(n-1):
    a = lst[i] - a
    print(a)