import sys
sys.stdin = open('9655_input.txt')

input = sys.stdin.readline

n = int(input())
if n % 2 == 0:
    print('CY')
else:
    print('SK')