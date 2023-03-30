import sys
sys.stdin = open('2004_input.txt')

input = sys.stdin.readline

def two(k):
    cnt = 0
    while k != 0:
        k = k // 2
        cnt += k
    return cnt

def five(k):
    cnt = 0
    while k != 0:
        k = k // 5
        cnt += k
    return cnt

n, m = map(int, input().split())

print(min((two(n)- two(n-m)-two(m)), (five(n)- five(n-m)-five(m))))


