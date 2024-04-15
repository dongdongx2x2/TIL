import sys
sys.stdin = open('16120_input.txt')

input = sys.stdin.readline

word = input().rstrip()

stack = []

for char in word:
    stack.append(char)

    if len(stack) >= 4 and ''.join(stack[-4:]) == "PPAP":
        for _ in range(3):
            stack.pop()

if "".join(stack) == "P":
    print("PPAP")
else:
    print("NP")

