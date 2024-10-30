import sys
sys.stdin = open('5397_input.txt')

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    keylog = input().rstrip()
    left_stack = []
    right_stack = []

    for char in keylog:
        if char == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif char == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        elif char == '-':
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(char)

    print(''.join(left_stack + right_stack[::-1]))