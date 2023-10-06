import sys
sys.stdin = open("9237_input.txt")

input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))
lst.sort(reverse=True)

for i in range(N):
    lst[i] = lst[i] + i + 1

print(max(lst) + 1)