import sys
sys.stdin = open('2263_input.txt')

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def find(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return []

    root = postorder[post_end]
    print(root, end=" ")
    root_index = inorder_index[root]

    left_tree_size = root_index - in_start

    find(in_start, root_index - 1, post_start, post_start + left_tree_size - 1)
    find(root_index + 1, in_end, post_start + left_tree_size, post_end - 1)


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

inorder_index = {value: idx for idx, value in enumerate(inorder)}

preorder = find(0, n-1, 0, n-1)