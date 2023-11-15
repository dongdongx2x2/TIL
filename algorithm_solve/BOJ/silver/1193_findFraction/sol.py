import sys

sys.stdin = open('1193_input.txt')

input = sys.stdin.readline

num = int(input())
line = 1

while num > line:
    num -= line
    line += 1

if line % 2:
    a = line - num + 1
    b = num
else:
    a = num
    b = line - num + 1

print(f'{a}/{b}')
