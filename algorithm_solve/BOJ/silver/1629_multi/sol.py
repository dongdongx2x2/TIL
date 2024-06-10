import sys
sys.stdin = open('1629_input.txt')

input = sys.stdin.readline

a, b, c = map(int, input().split())

def multi (a, b):
    if b == 1:
        return a % c
    else:
        tem = multi(a, b // 2)
        if b % 2 == 0:
            return (tem**2) % c
        else:
            return (tem**2*a) % c

print(multi(a,b))