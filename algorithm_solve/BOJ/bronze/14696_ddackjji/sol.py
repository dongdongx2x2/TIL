import sys
sys.stdin = open('14696_input.txt')

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    lista = list(map(int, input().split()))
    na = lista.pop(0)
    listb = list(map(int, input().split()))
    nb = listb.pop(0)
    lista.sort()
    listb.sort()
    if lista == listb:
        print('D')
    for i in range(4, 0, -1):
        if lista.count(i) > listb.count(i):
            print('A')
            break
        elif lista.count(i) < listb.count(i):
            print('B')
            break




