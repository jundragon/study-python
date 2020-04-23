# 01타일
# https://www.acmicpc.net/problem/1904
import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')

if __name__ == '__main__':
    N = int(input())
    tile = [0] * 1000001
    tile[1] = 1
    tile[2] = 2
    for i in range(3, N+1):
        tile[i] = (tile[i-1] + tile[i-2]) % 15746
    print(tile[N])