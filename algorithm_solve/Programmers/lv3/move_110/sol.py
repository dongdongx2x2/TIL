# https://school.programmers.co.kr/learn/courses/30/lessons/77886

def solution(s):
    def process(x):
        stack = []
        count_110 = 0
        
        # 1. "110" 제거 및 개수 세기
        for char in x:
            if len(stack) >= 2 and char == '0' and stack[-2:] == ['1', '1']:
                stack.pop()
                stack.pop()
                count_110 += 1
            else:
                stack.append(char)
        
        # 2. 남은 문자열에서 마지막 '0' 찾기
        for i in range(len(stack) - 1, -1, -1):
            if stack[i] == '0':
                return ''.join(stack[:i+1]) + '110' * count_110 + ''.join(stack[i+1:])
        
        # 3. '0'이 없는 경우 맨 앞에 삽입
        return '110' * count_110 + ''.join(stack)
    
    return [process(x) for x in s]