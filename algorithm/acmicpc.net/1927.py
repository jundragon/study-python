# 최소 힙
# https://www.acmicpc.net/problem/1927
import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')


import heapq


if __name__ == '__main__':
    N = int(input())
    heap = []
    result = []

    for _ in range(N):
        num = int(input())
        if num == 0:
            if heap:
                result.append(heapq.heappop(heap))
            else:
                result.append(0)
        else:
            heapq.heappush(heap, num)

    for data in result:
        print(data)