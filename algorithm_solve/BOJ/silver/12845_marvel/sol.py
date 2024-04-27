import sys
sys.stdin = open('12845_input.txt')

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort(reverse=True)

level = lst[0]
gold = 0

for c in lst[1:]:
    gold += level + c
    if level >= c:
        pass
    else:
        level = lst
print(gold)