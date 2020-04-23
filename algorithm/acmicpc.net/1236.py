# 성 지키기
# https://www.acmicpc.net/problem/1236
import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')

if __name__ == '__main__':
    row, col = map(int, input().split())

    row_state = [1 for _ in range(row)]
    col_state = [1 for _ in range(col)]

    for i in range(row):
        state = input()
        for j in range(len(state)):
            if state[j] == 'X':
                col_state[j] = 0
                row_state[i] = 0

    print(max(sum(row_state), sum(col_state)))


