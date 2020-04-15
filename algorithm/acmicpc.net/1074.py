# Z
# https://www.acmicpc.net/problem/1074
import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')

def Z(size, r, c):
    global result
    if size == 1:
        return 0

    if size == 2:
        if r == R and c == C:
            print(result)
            return
        result += 1
        if r == R and c + 1 == C:
            print(result)
            return
        result += 1
        if r + 1 == R and c == C:
            print(result)
            return
        result += 1
        if r + 1 == R and c + 1 == C:
            print(result)
            return
        result += 1
        return

    Z(size / 2, r, c)
    Z(size / 2, r, c + size/2)
    Z(size / 2, r + size/2, c)
    Z(size / 2, r + size/2, c + size/2)

if __name__ == '__main__':
    N, R, C = map(int, input().split())
    result = 0
    Z(2**N, 0, 0)

