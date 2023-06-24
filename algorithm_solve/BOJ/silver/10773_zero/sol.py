import sys
sys.stdin = open('10773_input.txt')

input = sys.stdin.readline

K = int(input())

tem = []
for _ in range(K):
    a = int(input())
    if a == 0:
        tem.pop()
    else:
        tem.append(a)
print(sum(tem))