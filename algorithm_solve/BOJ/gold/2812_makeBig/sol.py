import sys
sys.stdin = open('2812_input.txt')

input = sys.stdin.readline

n, k = map(int, input().split())

number = list(input().rstrip())

stack = []

for num in number:
    while stack and num > stack[-1] and k > 0:
        stack.pop()
        k -= 1
    stack.append(num)

if k > 0:
    print(''.join(stack[:-k]))
else:
    print(''.join(stack))
