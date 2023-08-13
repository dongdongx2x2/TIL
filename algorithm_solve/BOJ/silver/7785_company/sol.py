import sys
sys.stdin = open('7785_input.txt')

input = sys.stdin.readline

n = int(input())
tem = {}

for _ in range(n):
    a, b = map(str, input().split())

    if b == "enter":
        tem[a] = b
    else:
        del tem[a]

a = sorted(tem.keys(), reverse=True)

for i in a:
    print(i)

