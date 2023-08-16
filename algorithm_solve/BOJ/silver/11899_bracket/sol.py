import sys
sys.stdin = open('11899_input.txt')

input = sys.stdin.readline

a = input().rstrip()

while "()" in a:
    a = a.replace("()","")
print(len(a))