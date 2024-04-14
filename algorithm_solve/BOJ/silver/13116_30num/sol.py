import sys
sys.stdin = open('13116_input.txt')

input = sys.stdin.readline

t = int(input())

for i in range(t):
    a, b = map(int, input().split())

    while 1:
        if a > b:
            a //= 2

        elif a < b:
            b //= 2

        else:
            print(a*10)
            break