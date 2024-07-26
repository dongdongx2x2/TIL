import sys
sys.stdin = open('12871_input.txt')

input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

if s * len(t) == t * len(s):
    print(1)

else:
    print(0)