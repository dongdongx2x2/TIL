import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):

    N = int(input())
    cal = input()

    stack = [] # 연산자들을 담아둘 스택택
    result = '' # 최종 결과값

    #전체 식 순회
    for char in cal:
        # 연산자들이면
        if char == '+':
            while stack and stack[-1] == '+':
                result += stack.pop()
            stack.append(char)
        else:
            result += char
    while stack:
        result += stack.pop()
    # print(result)
    # print(stack)
    stack2 = []
    result2 = 0

    for char in result:
        if char != '+':
            stack.append(char)
        else:
            x = int(stack.pop())
            y = int(stack.pop())
            stack.append(x+y)
    result2 = stack.pop()
    print(f'#{tc} {result2}')