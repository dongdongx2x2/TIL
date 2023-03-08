import sys
sys.stdin = open('9012_input.txt')

input = sys.stdin.readline


def VPS(lst):
    stack = []

    for i in lst:
        if i == '(':
            stack.append(i)
        else: # ')' 일떄
            if not stack:  # 스택이 없는데 ') 나오면 NO
                return 'NO'
            else:  # 스택이 있는 상태고
                a = stack.pop() #')'를 뽑앗을떄
                if a == ')':
                    return 'NO'
    if stack:
        return 'NO'
    else:
        return 'YES'
T = int(input())

for _ in range(T):

    lst = list(input().rstrip())

    print(VPS(lst))


