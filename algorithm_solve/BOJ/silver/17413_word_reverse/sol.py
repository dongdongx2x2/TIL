import sys
sys.stdin = open('17413_input.txt')

input = sys.stdin.readline


word = input().rstrip()
# print(word)
tem =''
result = ''
flag = False

for c in word:
    if flag == False:
        if c == '<':
            tem += c
            flag = True
        elif c == ' ':
            tem += c
            result += tem
            tem = ''
        else:
            tem = c + tem

    else: # True일떄
        tem += c
        if c == '>':
            result += tem
            tem = ''
            flag = False

result = result + tem
print(result)