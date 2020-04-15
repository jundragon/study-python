# 소트인사이드
# https://www.acmicpc.net/problem/1427
import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')

if __name__ == '__main__':
    N = int(input())
    data = []
    while N >= 10:
        N, d = divmod(N, 10)
        data.append(d)
    data.append(N)
    data.sort(reverse=True)
    print("".join(map(str, data)))
