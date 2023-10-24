import sys
sys.stdin = open('1431_input.txt')

input = sys.stdin.readline

n = int(input())

lst = []

for _ in range(n):
    tem = list(input().rstrip())

    sm = 0

    for i in tem:
        if i.isdigit():
            sm += int(i)
    lst.append((''.join(tem), len(tem), sm))

lst.sort(key=lambda x:(x[1], x[2], x[0]))

for i in lst:
    print(i[0])



