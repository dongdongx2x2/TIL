import sys
sys.stdin = open('25757_input.txt')

input = sys.stdin.readline

n, k = input().split()

lst = [input() for _ in range(int(n))]
lst = list(set(lst))

if k == "Y":
    print(len(lst))
elif k == "F":
    print(len(lst) // 2)
else:
    print(len(lst) // 3)