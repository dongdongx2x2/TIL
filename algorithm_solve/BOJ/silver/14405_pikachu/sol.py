import sys
sys.stdin = open('14405_input.txt')

input = sys.stdin.readline

word = input().rstrip()

word = word.replace("pi", " ")
word = word.replace("ka", " ")
word = word.replace("chu", " ")

if len(word.strip()) == 0:
    print("YES")
else:
    print("NO")