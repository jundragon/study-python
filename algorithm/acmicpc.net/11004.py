# K번째 수
# https://www.acmicpc.net/problem/11004
import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')

if __name__ == '__main__':
    N, K = map(int, input().split())
    array = list(map(int, input().split()))

    array.sort()
    print(array[K-1])