import sys
sys.stdin = open('1254_input.txt')

input = sys.stdin.readline

S = input().rstrip()

n = len(S)

for i in range(n):
    if S[i:] == S[i:][::-1]:
        print(n+i)
        break