import sys
sys.stdin = open('11728_input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = (A + B)
ans.sort()

print(*ans)