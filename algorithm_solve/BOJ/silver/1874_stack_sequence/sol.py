import sys
sys.stdin = open('1874_input.txt')

input = sys.stdin.readline

n = int(input())


lst = []
for _ in range(n):
    lst.append(int(input()))

stack = []
result = ''

for i in range(1,n+1):
    stack.append(i)
    result += '+'
    while stack[-1] == lst[0]:
        stack.pop()
        lst.pop(0)
        result += '-'
        if not stack:
            break
if result.count('-') != result.count('+'):
    print('NO')
else:
    for i in result:
        print(i)


