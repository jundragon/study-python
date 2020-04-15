# 좌표 정렬하기
# https://www.acmicpc.net/problem/11650
import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')

if __name__ == '__main__':
    N = int(input())
    coords = []
    for _ in range(N):
        coord = tuple(map(int, input().split()))
        coords.append(coord)

    coords.sort()
    # coords.sort(key=lambda x: x[1])
    # coords.sort(key= lambda x: x[0])

    for coord in coords:
        print(coord[0], coord[1])