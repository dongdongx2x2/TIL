import sys
sys.stdin = open('11399_input.txt')

input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))

lst.sort()

cnt = 0

for i in range(1, N+1):
    cnt += sum(lst[:i])

print(cnt)