import sys
sys.stdin = open('1181_input.txt')

input = sys.stdin.readline

N = int(input())

lst = list(set(input().rstrip() for _ in range(N)))
lst.sort()
lst.sort(key=len)
for i in lst:
    print(i)