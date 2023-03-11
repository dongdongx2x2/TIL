import sys
sys.stdin = open('1406_input.txt')
input = sys.stdin.readline

word = list(input().rstrip())

n = int(input())

cs = len(word)

for _ in range(n):
    a = input().rstrip()

    if a == 'L':
        cs -= 1
        if cs < 0:
            cs = 0

    elif a == 'D':
        cs += 1
        if cs > len(word):
            cs = len(word)

    elif a == 'B':
        if cs == 0:
            continue
        else:
            word.pop(cs-1)
            cs = cs-1

    else:
        word.insert(cs, a[-1])
        cs += 1

print(''.join(word))