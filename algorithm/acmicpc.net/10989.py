# 수 정렬하기 3
# https://www.acmicpc.net/problem/10989
import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')

# if __name__ == '__main__':
#     N = int(input())
#
#     numbers = []
#     for _ in range(N):
#         num = int(input())
#         numbers.append(num)
#
#     numbers.sort()
#
#     for num in numbers:
#         print(num)
if __name__ == '__main__':
    N = int(input())
    numbers = [0] * 10001
    for _ in range(N):
        num = int(sys.stdin.readline())
        numbers[num] += 1

    for i in range(10001):
        if numbers[i] != 0:
            for j in range(numbers[i]):
                print(i)