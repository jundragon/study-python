# 트로피 진열
# https://www.acmicpc.net/problem/1668
import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')

if __name__ == '__main__':
    N = int(input())
    array = []
    for _ in range(N):
        array.append(int(input()))

    left = 1
    left_max = array[0]
    right = 1
    right_max = array[-1]

    for i in range(1, len(array)):
        if array[i] > left_max:
            left_max = array[i]
            left += 1
    for i in range(len(array)-2, -1, -1):
        if array[i] > right_max:
            right_max = array[i]
            right += 1

    print(left)
    print(right)