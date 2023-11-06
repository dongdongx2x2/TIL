import sys
sys.stdin = open('2870_input.txt')

input = sys.stdin.readline

n = int(input())

lst = []

for _ in range(n):
    ans = ''
    num = input().rstrip()
    for i in num:
        if i.isdigit():
            ans += i
        else:
            if ans != '':
                lst.append(int(ans))
                ans = ''
    if ans != '':
        lst.append(int(ans))

lst.sort()
for i in lst:
    print(i)