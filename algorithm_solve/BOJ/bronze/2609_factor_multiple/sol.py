import sys
sys.stdin = open('2609_input.txt')

input = sys.stdin.readline

n1, n2 = map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a

    else:
        return gcd(b, a%b)

print(gcd(n1,n2))
print(n1*n2//gcd(n1,n2))
