import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    cal = list(input().split())

    stack = []
    result = 0

    cnt = 0   #숫자가 몇갠지 세는
    for i in cal:
        if i not in '+-*/.':
            cnt += 1

    if len(cal) == cnt*2: # 연산자는 숫자개수 보다 1작아야 연산이됨
                          # cal에는 '.'도 있으니까 숫자갯수랑 숫자외의 갯수가 같아야함
                          # cal 길이는 숫자갯수의 2배 되야 에러가안남
                          # 2배가안되는거는 에러 처리
        for char in cal:
            if char == '.':
                continue
            elif char not in '+-*/':
                stack.append(int(char))
                # print(stack)
            else:
                x = stack.pop()
                y = stack.pop()
                if char == '+':
                    stack.append(y + x)
                elif char == '-':
                    stack.append(y - x)
                elif char == '*':
                    stack.append(y * x)
                elif char == '/':
                    stack.append(y // x)
        print(f'#{tc}', *stack)
    else:
        print(f'#{tc} error')