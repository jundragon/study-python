# 주사위 네개
# https://www.acmicpc.net/problem/2484
import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')


def reward():
    arr = sorted(list(map(int, input().split())))
    if len(set(arr)) == 1:
        return arr[0] * 5000 + 50000
    if len(set(arr)) == 2:
        if arr[1] == arr[2]:
            return arr[1] * 1000 + 10000
        return (arr[1] + arr[2]) * 500 + 2000
    for i in range(3):
        if arr[i] == arr[i+1]:
            return arr[i] * 100 + 1000
    return arr[-1] * 100


if __name__ == '__main__':
    N = int(input())
    print(max(reward() for i in range(N)))
