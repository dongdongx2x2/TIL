import sys
sys.stdin = open('20186_input.txt')

input = sys.stdin.readline

n, k = map(int, input().split())

lst = sorted(list(map(int, input().split())))

sm = 0

for i in range(1, k + 1):
    sm += lst[-i] - i + 1
print(sm)