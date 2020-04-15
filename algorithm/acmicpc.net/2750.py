# 수 정렬하기
# https://www.acmicpc.net/problem/2750
import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')

if __name__ == '__main__':
    N = int(input())
    numbers = []
    for _ in range(N):
        numbers.append(int(input()))

    numbers.sort()
    for n in numbers:
        print(n)