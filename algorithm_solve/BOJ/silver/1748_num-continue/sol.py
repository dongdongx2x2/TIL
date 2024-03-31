import sys
sys.stdin = open('1748_input.txt')

input = sys.stdin.readline

n = input().rstrip()
tem = len(n) - 1

answer = 0

for i in range(tem):
    answer += 9 * (10 ** i) * (i + 1)
    i += 1
answer += ((int(n) - (10 ** tem)) + 1) * (tem + 1)

print(answer)