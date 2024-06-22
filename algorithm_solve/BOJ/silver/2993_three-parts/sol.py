import sys

sys.stdin = open('2993_input.txt')

input = sys.stdin.readline

s = input().rstrip()
result = s

n = len(s)
for i in range(1, n):
    for j in range(i + 1, n):
        result = min(result, s[:i][::-1] + s[i:j][::-1] + s[j:][::-1])
print(result)
