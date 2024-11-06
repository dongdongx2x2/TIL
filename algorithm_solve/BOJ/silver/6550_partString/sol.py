import sys
sys.stdin = open('6550_input.txt')

input = sys.stdin.readline

def is_subsequence(s, t):
    i = 0
    for char in t:
        if i < len(s) and char == s[i]:
            i += 1
    return i == len(s)

while True:
    try:
        s, t = input().split()
        if is_subsequence(s, t):
            print("Yes")
        else:
            print("No")
    except:
        break