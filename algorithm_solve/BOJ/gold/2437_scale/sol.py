import sys
sys.stdin = open('2437_input.txt')

input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))
lst.sort()

target = 1
# print(lst)
for i in lst:
    if target < i:
        break
    target += i
    # print(target)

print(target)