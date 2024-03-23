import sys
sys.stdin = open('2535_input.txt')

input = sys.stdin.readline

n = int(input())

lst = [list(map(int, input().split())) for _ in range(n)]

lst.sort(key = lambda x: -x[2])

print(*lst[0][:2])
print(*lst[1][:2])

k = 2
if lst[0][0] == lst[1][0]:
    while lst[0][0] == lst[k][0]:
        k += 1
print(*lst[k][:2])