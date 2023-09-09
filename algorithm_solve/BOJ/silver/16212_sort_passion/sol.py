import sys
sys.stdin = open('16212_input.txt')

input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))

lst.sort()

for i in lst:
    print(i, end=" ")