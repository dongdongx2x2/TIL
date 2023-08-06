import sys
sys.stdin = open('11478_input.txt')

input = sys.stdin.readline

S = input().rstrip()
sset = set()

for i in range(len(S)):
    for j in range(i, len(S)):
        sset.add(S[i:j+1])
print(len(sset))