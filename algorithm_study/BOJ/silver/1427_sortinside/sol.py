import sys
sys.stdin = open('1427_input.txt')

input = sys.stdin.readline

lst = list(input().rstrip())

lst.sort(reverse=True)
for i in lst:
    print(i, end='')
