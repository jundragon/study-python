# SHA-256
# https://www.acmicpc.net/problem/10930
import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')

import hashlib

if __name__ == '__main__':
    data = input()
    print(hashlib.sha256(data.encode()).hexdigest())
