# 평범한 배낭
# https://www.acmicpc.net/problem/12865
import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')

if __name__ == '__main__':
    N, K = map(int, input().split())
    dp = [[0] * (K+1) for _ in range(N+1)]

    for i in range(1, N+1):
        W, V = map(int, input().split())

        for j in range(1, K+1):
            if j >= W:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-W] + V)

    print(dp[N][K])
