# DFS와 BFS
# https://www.acmicpc.net/problem/1260
import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')


if __name__ == '__main__':
    N = int(input())
    stairs = []
    for _ in range(N):
        stairs.append(int(input()))

    score = []
    score.append(stairs[0])
    score.append(stairs[1] + stairs[0])
    score.append(max(stairs[1]+stairs[2], stairs[0]+stairs[2]))

    for i in range(3, N):
        a = stairs[i]+score[i-2]
        b = stairs[i]+stairs[i-1]+score[i-3]
        score.append(max(stairs[i]+score[i-2], stairs[i]+stairs[i-1]+score[i-3]))
        print(score)

    print(stairs)

