import sys
sys.stdin = open('1235_input.txt')

input = sys.stdin.readline

n = int(input())

lst = [input().rstrip() for _ in range(n)]

k = 1

while True:
    sset = set()
    for i in lst:
        sset.add(i[-k:])
    if len(sset) == n:
        break
    k += 1
print(k)