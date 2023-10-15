import sys
sys.stdin = open('2548_input.txt')

input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

lst.sort()

if N % 2:
    print(lst[N//2])
else:
    print(lst[N//2-1])