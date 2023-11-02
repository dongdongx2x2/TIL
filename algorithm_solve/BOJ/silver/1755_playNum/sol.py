import sys
sys.stdin = open('1755_input.txt')

input = sys.stdin.readline

m, n = map(int, input().split())

num = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '0': 'zero'}

lst = []

for i in range(m, n + 1):
    a = ' '.join([num[j] for j in str(i)])
    lst.append([i, a])

lst.sort(key=lambda x: x[1])

for i in range(len(lst)):
    if i % 10 == 0 and i != 0:
        print()
    print(lst[i][0], end=' ')
