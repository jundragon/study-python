# 가장 긴 증가하는 부분 수열 (LIS)
# https://www.acmicpc.net/problem/11053
import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')

if __name__ == '__main__':
    N = int(input())
    dp = [1] * N
    arr = list(map(int, input().split()))
    for i in range(1, N):
        for j in range(0, i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j]+1)

    print(max(dp))

    # array = list(map(int, input().split()))
    # lenght = 1
    # max_val = array[0]
    # for idx in range(1, len(array)):
    #     if max_val < array[idx]:
    #         max_val = array[idx]
    #         lenght += 1
    #
    # print(lenght)
