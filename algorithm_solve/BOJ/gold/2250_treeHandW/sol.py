import sys
sys.stdin = open('2250_input.txt')

input = sys.stdin.readline

def inorder(node, level):
    global column
    if node == -1:
        return

    inorder(tree[node][0], level + 1)

    column += 1
    if level not in level_min:
        level_min[level] = column
    level_max[level] = column

    inorder(tree[node][1], level + 1)

n = int(input())
tree = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)

for _ in range(n):
    data, left, right = map(int, input().split())
    tree[data] = [left, right]
    if left != -1:
        parent[left] = data
    if right != -1:
        parent[right] = data

root = 1
for i in range(1, n + 1):
    if parent[i] == 0:
        root = i
        break

column = 0
level_min = {}
level_max = {}

inorder(root, 1)

max_width = 0
max_level = 0

for level in range(1, len(level_max) + 1):
    width = level_max[level] - level_min[level] + 1
    if width > max_width:
        max_width = width
        max_level = level

print(max_level, max_width)