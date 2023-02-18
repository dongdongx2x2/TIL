import sys
sys.stdin = open('input.txt')

for tc in range(1,11):

    N, data = input().split()

    stack = [] # 숫자를 하나하나 넣을 빈 스택

    for i in data:
        if not stack: # 스택이 비었따면
            stack.append(i) # 스택에 추가
        elif stack and stack[-1] != i: # 스택에 값이 있고 스택의 top이 i랑 같지않다면
            stack.append(i) # i를 스택에 추가
        elif stack and stack[-1] == i: # 스택에 값이 있는데 스택의 top이 i랑 같다면
            stack.pop() #스택의 top을 제거
    result = ''
    for i in stack:
        result += i

    print(f'#{tc} {result}')
