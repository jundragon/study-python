# 거스름돈
# https://www.acmicpc.net/problem/5585
import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')

if __name__ == '__main__':
    N = int(input())
    coins = [500, 100, 50, 10, 5, 1]
    count = 0

    money = 1000 - N
    while money > 0:
        for coin in coins:
            if money >= coin:
                a, b = divmod(money, coin)
                count += a
                money = b

    print(count)