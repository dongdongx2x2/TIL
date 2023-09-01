import sys
sys.stdin = open('1316_input.txt')

input = sys.stdin.readline

N = int(input())

cnt = N
for _ in range(N):
    word = input().rstrip()

    for j in range(len(word)-1):
        if word[j] == word[j+1]:
            continue
        if word[j] in word[j+1:]:
            cnt -= 1
            break
print(cnt)