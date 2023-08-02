import sys
sys.stdin = open('9935_input.txt')

input = sys.stdin.readline

words = list(input().rstrip())
bomb = list(input().rstrip())
len_bomb = len(bomb)

stack = []

for i in range(len(words)):
    stack.append(words[i])
    # print(stack[-len_bomb:])
    if stack[-len_bomb:] == bomb:
        for _ in range(len_bomb):
            stack.pop()
if stack:
    print(''.join(stack))
else:
    print('FRULA')
