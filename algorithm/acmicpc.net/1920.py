# 수 찾기
# https://www.acmicpc.net/problem/1920
import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')

if __name__ == '__main__':
    N = int(input())
    A = set(map(int, input().split())) # refer 데이터는 set 자료형을 사용하여 중복을 없앤다.
    M = int(input())
    data = list(map(int, input().split()))

    for d in data:
        if d in A:
            print("1")
        else:
            print("0")