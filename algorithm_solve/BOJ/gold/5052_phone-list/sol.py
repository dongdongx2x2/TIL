import sys
sys.stdin = open('5052_input.txt')

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    lst = []
    for _ in range(n):
        lst.append(input().rstrip())
    lst.sort()

    flag = True
    for i in range(n-1):
        if lst[i] == lst[i+1][:len(lst[i])]:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")

