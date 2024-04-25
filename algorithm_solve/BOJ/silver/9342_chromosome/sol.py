import sys,re
sys.stdin = open('9342_input.txt')

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    chromosome = input().rstrip()

    pattern = re.compile('^[A-F]?A+F+C+[A-F]?$')

    if pattern.match(chromosome):
        print("Infected!")
    else:
        print("Good")