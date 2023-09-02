import sys
sys.stdin = open('16499_input.txt')

input = sys.stdin.readline

N = int(input())
lst = []

for _ in range(N):
    word = list(input().rstrip())
    word.sort()

    if word not in lst:
        lst.append(word)
print(len(lst))
