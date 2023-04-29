import sys
sys.stdin = open('2504_input.txt')

input = sys.stdin.readline


word = input().rstrip()
word = word.replace('()', '2')
word = word.replace('[]', '3')
# print(word)

stack = []
for c in word:
    if c == '(':
        stack.append(c)
    elif c.isdigit():
        if len(stack) >= 1 and stack[-1].isdigit():
            a = stack.pop()
            stack.append(str(int(c) + int(a)))
        else:
            stack.append(c)
    elif c == '[':
        stack.append(c)
    elif c == ')':
        if len(stack) >= 2 and stack[-1].isdigit() and stack[-2] == '(':
            a = stack.pop()
            stack.pop()
            stack.append(str(int(a)*2))
            if len(stack) >= 2 and stack[-2].isdigit():
                b = stack.pop()
                c = stack.pop()
                stack.append(str(int(b)+int(c)))
        else:
            stack.append(c)
    elif c == ']':
        if len(stack) >= 2 and stack[-1].isdigit() and stack[-2] == '[':
            a = stack.pop()
            stack.pop()
            stack.append(str(int(a)*3))
            if len(stack) >= 2 and stack[-2].isdigit():
                b = stack.pop()
                c = stack.pop()
                stack.append(str(int(b)+int(c)))
        else:
            stack.append(c)

result = ''.join(stack)
if result.isdigit():
    print(result)
else:
    print(0)