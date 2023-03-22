import sys
sys.stdin = open('1935_input.txt')

input = sys.stdin.readline

N = int(input())

cal = input().rstrip()

alpabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

dic = {}

for i in range(N):

    dic[alpabet[i]] = int(input())

stack = []

for c in cal:

    if c in alpabet:
        stack.append(dic[c])

    else:
        if c == '+':
            x = stack.pop()
            y = stack.pop()
            a = y + x

        elif c == '-':
            x = stack.pop()
            y = stack.pop()
            a = y - x

        elif c == '*':
            x = stack.pop()
            y = stack.pop()
            a = y * x

        elif c == '/':
            x = stack.pop()
            y = stack.pop()
            a = y / x

        stack.append(a)

print('%.2f' % stack[0])
