import sys
sys.stdin = open("14729_input.txt")

input = sys.stdin.readline

N = int(input())

lst = []

for _ in range(N):
    lst.append(float(input()))
lst.sort()
for i in range(7):
    print(f"{lst[i]:.3f}")