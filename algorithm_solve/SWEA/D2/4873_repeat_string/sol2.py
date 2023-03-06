import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T +1):
    word = input()

    stack = []

    for char in word:
        if not stack:
            stack.append(char)
        elif stack and stack[-1] != char:
            stack.append(char)
        elif stack and stack[-1] == char:
            stack.pop()

    print(f'#{tc} {len(stack)}')
