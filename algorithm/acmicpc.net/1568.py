# 새
# https://www.acmicpc.net/problem/1568
import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')

if __name__ == '__main__':
    N = int(input())

    sing = 0
    time = 0
    while N > 0:
        sing += 1

        if N < sing:
            sing = 1
        N -= sing
        time += 1

    print(time)