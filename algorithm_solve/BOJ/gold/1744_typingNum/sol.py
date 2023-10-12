import sys
sys.stdin = open("1744_input.txt")

input = sys.stdin.readline

N = int(input())

lst = [int(input()) for _ in range(N)]

lst.sort()

sm = 0 # 총합

lst1 = [] # 음수 리스트
lst2 = [] # 양수 리스트

for i in lst:
    if i < 0:
        lst1.append(i)
    elif i == 0:
        if lst1:
            if len(lst1) % 2: # 홀수일떄
                lst1.pop()
    elif i == 1:
        sm += 1
    else:
        lst2.append(i)

if len(lst1) % 2: # 홀 수 일 때
    sm += lst1.pop() # 짝수가됨
    for j in range(0, len(lst1), 2):
        sm += lst1[j] * lst1[j+1]
else:
    for j in range(0, len(lst1), 2):
        sm += lst1[j] * lst1[j+1]

if len(lst2) % 2: # 홀수일 때
    sm += lst2[0]
    for j in range(1, len(lst2), 2):
        sm += lst2[j] * lst2[j+1]

else: # 짝수개일때
    for j in range(0, len(lst2), 2):
        sm += lst2[j] * lst2[j+1]
print(sm)