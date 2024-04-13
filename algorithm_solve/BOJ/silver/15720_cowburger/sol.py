import sys
sys.stdin = open('15720_input.txt')

input = sys.stdin.readline

b,c,d = map(int, input().split())

arrB = list(map(int, input().split()))
arrC = list(map(int, input().split()))
arrD = list(map(int, input().split()))

arrB.sort(reverse=True)
arrC.sort(reverse=True)
arrD.sort(reverse=True)

before = sum(arrB) + sum(arrC) + sum(arrD)

cnt = min(len(arrB), len(arrC), len(arrD))
after = before - (sum(arrB[:cnt]) + sum(arrC[:cnt]) + sum(arrD[:cnt])) // 10

print(before)
print(after)