# https://school.programmers.co.kr/learn/courses/30/lessons/76502

def is_valid(s):
    stack = []
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack:
                return False
            if char == ')' and stack[-1] != '(':
                return False
            if char == ']' and stack[-1] != '[':
                return False
            if char == '}' and stack[-1] != '{':
                return False
            stack.pop()
    return len(stack) == 0

def solution(s):
    count = 0
    for i in range(len(s)):
        rotated = s[i:] + s[:i]
        if is_valid(rotated):
            count += 1
    return count