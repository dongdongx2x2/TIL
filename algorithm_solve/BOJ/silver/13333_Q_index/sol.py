import sys
sys.stdin = open('13333_input.txt')

input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))
lst.sort()

for i in range(n, -1, -1):
    if i <= lst[-i]:
        print(i)
        break