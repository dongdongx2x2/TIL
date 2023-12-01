import sys
sys.stdin = open('9656_input.txt')

input = sys.stdin.readline

n = int(input())

if n % 2:
    print("CY")
else:
    print("SK")