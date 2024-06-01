import sys
sys.stdin = open('2941_input.txt')

input = sys.stdin.readline

lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input().rstrip()

for i in lst:
    word = word.replace(i, '*')
print(len(word))