import sys
sys.stdin = open('1620_input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())

dic = {}

for i in range(1, n+1):
    a = input().rstrip()
    dic[i] = a
    dic[a] = i

for i in range(m):
    q = input().rstrip()
    if q.isdigit():
        print(dic[int(q)])

    else:
        print(dic[q])