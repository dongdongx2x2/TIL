import sys
sys.stdin = open('9519_input.txt')

input = sys.stdin.readline

x = int(input())
word = list(input().rstrip())

n = len(word)
pattern = [word[:]]

while True:
    f = word[:n//2+1]
    b = word[n//2+1:]

    word = []
    for _ in range(len(b)):
        word.append(f.pop(0))
        word.append(b.pop())
    word += f
    if word == pattern[0]:
        break
    pattern.append(word)
    # print(word)

pattern = [pattern[0]] + pattern[1:][::-1]
# print(pattern)
print("".join(pattern[x % len(pattern)]))
