import sys
sys.stdin = open('1232_input.txt')

def postorder(node): # 후위계산 하기위해 후위순회해야함
    global lst
    if node:
        postorder(data[node][2])
        postorder(data[node][3])
        lst.append(data[node][1])

def cal(lst):
    stack = []
    for i in lst:
        if type(i) == int:
            stack.append(i)
        else:
            a = stack.pop()
            b = stack.pop()
            if i == '-':
                stack.append(b - a)
            elif i == '+':
                stack.append(a + b)
            elif i == '*':
                stack.append(a * b)
            elif i == '/':
                stack.append(b//a)
    return stack[-1]

for tc in range(1,11):
    N = int(input())

    data = [list(map(lambda x: int(x) if x.isdecimal() else x, input().split()))for _ in range(N)]

    for arr in data:
        while len(arr) != 4:
            arr.append(0)
    data.insert(0, [0, 0, 0, 0])
    # pprint(data)
    lst = []
    postorder(1)

    print(f'#{tc} {cal(lst)}')
