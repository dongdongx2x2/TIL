import sys
sys.stdin = open('1393_input.txt')

input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def distance(x, y):
    return ((x - xs)**2 + (y- ys)**2) ** 0.5
xs, ys = map(int, input().split())

xe, ye, dx, dy = map(int, input().split())

ggcd = gcd(dx, dy)

dx, dy = dx // ggcd, dy // ggcd

cx, cy = xe, ye

while distance(cx, cy) > distance(cx + dx, cy + dy):
    cx += dx
    cy += dy

print(cx, cy)


