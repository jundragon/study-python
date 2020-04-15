# 블랙잭
# https://www.acmicpc.net/problem/2798
import sys
sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')

if __name__ == '__main__':
    N, M = map(int, input().split())
    cards = list(map(int, input().split()))

    cards.sort(reverse=True)
    result = 0
    length = len(cards)
    for i in range(length):
        if result == M:
            break
        for j in range(i+1, length):
            for k in range(j+1, length):
                val = cards[i] + cards[j] + cards[k]
                if val <= M:
                    result = max(result, val)

    print(result)
