# https://school.programmers.co.kr/learn/courses/30/lessons/60058

# 균형잡힌 괄호 문자열인지 확인하는 함수
# 조건에 맞는 재귀함수

def divide(p):
    cnt = [0, 0]

    for i in range(len(p)):
        if p[i] == '(':
            cnt[0] += 1
        else:
            cnt[1] += 1
        
        if cnt[0] == cnt[1]:
            return p[:i+1], p[i+1:]
        
def is_balance(word):
    stack = []
    
    for i in word:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            stack.pop()
    return True

def solution(p):
    if p == '':
        return ''
    
    u, v = divide(p)
    
    if is_balance(u):
        return u + solution(v)
    
    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        u = list(u[1:-1])

        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('

        answer += "".join(u)

        return answer