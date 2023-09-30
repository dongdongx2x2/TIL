import sys
sys.stdin = open('1448_input.txt')

input = sys.stdin.readline

n = int(input())

lst = []
for _ in range(n):
    lst.append(int(input()))

lst.sort(reverse=True)

for i in range(n-2):
    if lst[i] < lst[i+1] + lst[i+2]:
        print(lst[i] + lst[i+1] + lst[i+2])
        exit()
print(-1)