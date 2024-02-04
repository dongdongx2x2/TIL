import sys
sys.stdin = open('1735_input.txt')

input = sys.stdin.readline


def GCD(x, y):
    tem = x % y
    while tem:
        x = y
        y = tem
        tem = x % y
    return y

A, B = map(int, input().split())
C, D = map(int, input().split())
N = GCD(A*D + C*B, B*D)
print((A*D + C*B)//N, B*D//N)