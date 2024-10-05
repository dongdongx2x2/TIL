import sys
sys.stdin = open('9996_input.txt')

input = sys.stdin.readline

n = int(input())
pattern = input().split("*")
l = len(pattern[0]) + len(pattern[1])

for _ in range(n):
    arr = input()

    if len(arr) >= l and arr.startswith(pattern[0]) and arr.endswith(pattern[1]):
        print("DA")
    else:
        print("NE")