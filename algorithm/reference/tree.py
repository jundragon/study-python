import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')


class Node:
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right


def pre_order(node):
    print(node.root, end='')
    if node.left != '.':
        pre_order(tree[node.left])
    if node.right != '.':
        pre_order(tree[node.right])


def in_order(node):
    if node.left != '.':
        in_order(tree[node.left])
    print(node.root, end='')
    if node.right != '.':
        in_order(tree[node.right])


def post_order(node):
    if node.left != '.':
        post_order(tree[node.left])
    if node.right != '.':
        post_order(tree[node.right])
    print(node.root, end='')


if __name__ == '__main__':
    n = int(input())
    tree = {}
    for i in range(n):
        root, left, right = input().split()
        tree[root] = Node(root, left, right)

    pre_order(tree['A'])
    print()
    in_order(tree['A'])
    print()
    post_order(tree['A'])