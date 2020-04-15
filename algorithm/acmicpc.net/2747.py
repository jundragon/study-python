# 피보나치 수
# https://www.acmicpc.net/problem/2747
import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')

if __name__ == '__main__':
    N = int(input())
    fibonacci = []
    fibonacci.append(0)
    fibonacci.append(1)
    for i in range(2, N+1):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    print(fibonacci[-1])