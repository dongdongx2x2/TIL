import sys
sys.stdin = open('1251_input.txt')

input = sys.stdin.readline

word = input().rstrip()

lst = []

for i in range(1, len(word)-1):
    for j in range(i + 1, len(word)):
        a = word[:i][::-1]
        b = word[i:j][::-1]
        c = word[j:][::-1]
        n_word = a + b + c
        lst.append(n_word)
lst.sort()
print(lst[0])