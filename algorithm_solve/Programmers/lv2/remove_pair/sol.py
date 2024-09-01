# https://school.programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
            
    answer = 1 if not stack else 0

    return answer