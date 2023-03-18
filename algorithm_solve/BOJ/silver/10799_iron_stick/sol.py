import sys
sys.stdin = open('10799_input.txt')

input = sys.stdin.readline

stick = input().rstrip()

stick = stick.replace('()', '#')
tem = []
cnt = 0
for c in stick:

    if c == '(':
        tem.append(c)
        cnt += 1

    elif tem and c == '#':
        cnt += 1 * len(tem)

    elif tem and c == ')':
        tem.pop()

print(cnt)
