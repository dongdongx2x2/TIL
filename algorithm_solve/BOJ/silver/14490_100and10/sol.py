import sys
sys.stdin = open('14490_input.txt')

input = sys.stdin.readline

from math import gcd

a, b = map(int,input().split(":"))

print(int(a/gcd(a,b)), end='')
print(':',end='')
print(int(b/gcd(a,b)))