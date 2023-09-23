import sys
sys.stdin = open('11931_input.txt')

input = sys.stdin.readline

N = int(input())
lst = []

for _ in range(N):
    a = int(input())
    lst.append(a)

lst.sort(reverse=True)

for i in lst:
    print(i)