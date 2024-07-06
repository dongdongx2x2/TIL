import sys

sys.stdin = open('9417_input.txt')

input = sys.stdin.readline


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


n = int(input())

for _ in range(n):
    lst = list(map(int, input().split()))
    temlst = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if i != j:
                temlst.append(gcd(lst[i], lst[j]))
    print(max(temlst))
