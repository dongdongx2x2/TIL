import sys
sys.stdin = open('27964_input.txt')

input = sys.stdin.readline

n = int(input())
toppings = input().split()

cheese_count = set()

for topping in toppings:
    if topping.endswith("Cheese"):
        cheese_count.add(topping)

if len(cheese_count) >= 4:
    print("yummy")
else:
    print("sad")