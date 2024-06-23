import sys
sys.stdin = open('11008_input.txt')

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    s, p = input().split()
    s = s.replace(p, '.')

    print(len(s))