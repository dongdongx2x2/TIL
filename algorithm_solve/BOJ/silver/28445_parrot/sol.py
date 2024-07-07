import sys
sys.stdin = open('28445_input.txt')

input = sys.stdin.readline

dad_body, dad_tail = input().split()
mom_body, mom_tail = input().split()

body_colors = {dad_body, dad_tail, mom_body, mom_tail}
tail_colors = {dad_body, dad_tail, mom_body, mom_tail}

combinations = set()

for body in body_colors:
    for tail in tail_colors:
        combinations.add((body, tail))

sorted_combinations = sorted(combinations)

for body, tail in sorted_combinations:
    print(body, tail)