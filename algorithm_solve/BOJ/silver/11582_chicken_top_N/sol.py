import sys

sys.stdin = open('11582_input.txt')

input = sys.stdin.readline

N = int(input())
lst1 = list(map(int, input().split()))
k = int(input())

idx = N // k
lst2 = []

for i in range(0, N, idx):
    lst2 = lst1[i:i + idx]
    lst2.sort()
    for j in lst2:
        print(j, end=' ')
