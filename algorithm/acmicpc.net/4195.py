# 친구 네트워크
# https://www.acmicpc.net/problem/4195
import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')

def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    parent[y] = x

if __name__ == '__main__':
    parent = []

    # case = int(input())
    # for i in range(case):
    #     F = int(input())
    #     for _ in range(F):
    for i in range(0, 5):
        parent.append(i)

    union(1, 4)
    union(2, 4)

    for i in range(1, len(parent)):
        print(find(i), end=' ')
