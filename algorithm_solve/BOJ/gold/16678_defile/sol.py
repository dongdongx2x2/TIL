import sys
sys.stdin = open('16678_input.txt')

input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]

lst.sort()

tem = 1
hacker = 0

for num in lst:
    if num >= tem:
        hacker += num - tem
        tem += 1

print(hacker)