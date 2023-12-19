import sys
sys.stdin = open('1402_input.txt')

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    print("yes")