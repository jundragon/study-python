# 문서 검색
# https://www.acmicpc.net/problem/1543
import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')

if __name__ == '__main__':
    string = input()
    word = input()

    cnt = 0
    i = 0
    while string.find(word, i) != -1:
        i = string.find(word, i) + len(word)
        cnt += 1

    print(cnt)