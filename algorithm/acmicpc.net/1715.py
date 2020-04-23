# 카드 정렬하기
# https://www.acmicpc.net/problem/1715
import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')

import heapq

if __name__ == '__main__':
    N = int(input())
    cards = []
    for _ in range(N):
        cards.append(int(input()))

    heapq.heapify(cards)

    result = 0
    while len(cards) > 1:
        card1 = heapq.heappop(cards)
        card2 = heapq.heappop(cards)
        sum_val = card1 + card2
        result += sum_val
        heapq.heappush(cards, sum_val)

    print(result)