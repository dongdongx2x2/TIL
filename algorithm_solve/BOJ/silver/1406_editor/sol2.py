import sys
sys.stdin = open('1406_input.txt')
input = sys.stdin.readline

stack = list(input().rstrip())

n = int(input())


stack2 = []
for _ in range(n):
    a = input().rstrip()

    if a == 'L':
        if stack:
            stack2.append(stack.pop())

    elif a == 'D':
        if stack2:
            stack.append(stack2.pop())

    elif a == 'B':
        if stack:
            stack.pop()

    else:
        stack.append(a[-1])


print(''.join(stack + stack2[::-1]))
