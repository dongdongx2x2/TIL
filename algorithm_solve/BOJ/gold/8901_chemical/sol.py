import sys
sys.stdin = open('8901_input.txt')

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    ab, bc, ca = map(int, input().split())

    profits = []

    for ab_use in range(min(a, b) + 1):
        for bc_use in range(min(b - ab_use, c) + 1):
            ca_use = min(c - bc_use, a - ab_use)
            profit = ab_use * ab + bc_use * bc + ca_use * ca
            profits.append(profit)

    print(max(profits))