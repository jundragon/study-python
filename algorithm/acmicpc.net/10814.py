# 나이순 정렬
# https://www.acmicpc.net/problem/10814
import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')

if __name__ == '__main__':
    N = int(input())
    m_list = []
    for _ in range(N):
        member = input().split()
        m_list.append((int(member[0]), member[1]))

    m_list.sort(key= lambda x: x[0])
    for m in m_list:
        print(m[0], m[1])