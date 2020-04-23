# 트리 순회
# https://www.acmicpc.net/problem/1991
import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')


class Node:
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right

def pre_order(node):
    print(node, end='')
    if tree[node].left != '.':
        pre_order(tree[node].left)
    if tree[node].right != '.':
        pre_order(tree[node].right)

def in_order(node):
    if tree[node].left != '.':
        in_order(tree[node].left)
    print(node, end='')
    if tree[node].right != '.':
        in_order(tree[node].right)

def post_order(node):
    if tree[node].left != '.':
        post_order(tree[node].left)
    if tree[node].right != '.':
        post_order(tree[node].right)
    print(node, end='')

if __name__ == '__main__':
    N = int(input()) # 이진 트리의 노드의 개수

    tree = {}
    for _ in range(N):
        root, left, right = input().split()
        tree[root] = Node(root, left, right)

    pre_order('A')
    print()
    in_order('A')
    print()
    post_order('A')