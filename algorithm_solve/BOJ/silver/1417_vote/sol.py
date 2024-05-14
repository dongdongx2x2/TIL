import sys

sys.stdin = open('1417_input.txt')

input = sys.stdin.readline

n = int(input())
one = int(input())
vote = []

count = 0

for _ in range(n - 1):
    vote.append(int(input()))

vote.sort(reverse=True)

if n == 1:
    print(0)
else:

    while vote[0] >= one:
        one += 1
        vote[0] -= 1
        count += 1
        vote.sort(reverse=True)
    print(count)