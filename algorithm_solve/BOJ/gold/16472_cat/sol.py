import sys
sys.stdin = open('16472_input.txt')

input = sys.stdin.readline

n = int(input())
words = input().rstrip()

s, e = 0, 0
dic = {}
max_length = 0
while e < len(words):
    if words[e] in dic:
        dic[words[e]] += 1
    else:
        dic[words[e]] = 1

    while len(dic) > n:
        dic[words[s]] -= 1
        if dic[words[s]] == 0:
            del dic[words[s]]
        s += 1

    max_length = max(max_length, e - s + 1)
    e += 1

print(max_length)

