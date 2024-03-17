import sys
sys.stdin = open('2417_input.txt')

input = sys.stdin.readline

n = int(input())

s = 0
e = n

while s <= e:
    m = (s + e) // 2

    if m ** 2 < n:
        s = m + 1

    else:
        e = m - 1

print(s)