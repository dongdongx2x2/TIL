import sys

sys.stdin = open('1475_input.txt')

input = sys.stdin.readline

n = input().rstrip()

lst = [0] * 10

for i in n:
    if i == '6' or i == '9':
        if lst[6] <= lst[9]:
            lst[6] += 1
        else:
            lst[9] += 1
    else:
        lst[int(i)] += 1

print(max(lst))
