import sys
sys.stdin = open('6443_input.txt')

input = sys.stdin.readline

def dfs(idx, combi):
    if idx == len_word:
        print(combi)
        return

    for i in range(len_word):
        if not v[i]:
            tem = combi + word[i]

            if tem not in sset:
                v[i] = 1
                sset.add(tem)
                dfs(idx + 1, tem)
                v[i] = 0
n = int(input())

for _ in range(n):
    word = input().rstrip()
    word = sorted(word)
    len_word = len(word)

    v = [0] * len_word
    sset = set()
    dfs(0, "")
