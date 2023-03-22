import sys
sys.stdin = open('11656_input.txt')

input = sys.stdin.readline

word = input().rstrip()

result = []
for i in range(len(word)):
    result.append(word[i:])

for i in sorted(result):
    print(i)