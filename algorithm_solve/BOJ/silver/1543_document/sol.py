import sys
sys.stdin = open('1543_input.txt')

input = sys.stdin.readline

target = input().rstrip()
word = input().rstrip()

target = target.replace(word,"A")


print(target.count("A"))