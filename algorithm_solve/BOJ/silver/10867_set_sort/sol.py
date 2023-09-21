import sys
sys.stdin = open('10867_input.txt')

input = sys.stdin.readline

N = int(input())

lst = list(set(map(int, input().split())))
lst.sort()

for i in lst:
    print(i, end=" ")