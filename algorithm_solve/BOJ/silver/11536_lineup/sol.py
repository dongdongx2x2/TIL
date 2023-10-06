import sys
sys.stdin = open('11536_input.txt')

input = sys.stdin.readline

n = int(input())

lst = []

for _ in range(n):
    lst.append(input().rstrip())

if sorted(lst) == lst:
    print("INCREASING")
elif sorted(lst, reverse=True) == lst:
    print("DECREASING")
else:
    print("NEITHER")