import sys
sys.stdin = open('10828_input.txt')

input = sys.stdin.readline

N = int(input())


stack = []
for _ in range(N):
    x = input().rstrip()
    if x == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif x == 'size':
        print(len(stack))

    elif x == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif x == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    else:
        stack.append(x[5:])
