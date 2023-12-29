import sys
sys.stdin = open('3060_input.txt')

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))

    food = sum(lst)
    day = 1

    while n >= food:
        day += 1
        food *= 4
    print(day)