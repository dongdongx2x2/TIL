import sys
sys.stdin = open('1541_input.txt')

input = sys.stdin.readline

lst = input().split('-')

s = 0

for i in lst[0].split('+'):
    s += int(i)

for i in lst[1:]:
    for j in i.split('+'):
        s -= int(j)

print(s)