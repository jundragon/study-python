# 숨바꼭질
# https://www.acmicpc.net/problem/1697
import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')
from collections import deque


def bfs(pos):
    queue = deque()
    queue.append(pos)

    while queue:
        pos = queue.popleft()
        if pos == K:
            return arr[pos]
        for next_pos in (pos-1, pos+1, pos*2):
            if 0 <= next_pos < MAX and not arr[next_pos]:
                arr[next_pos] = arr[pos] + 1
                queue.append(next_pos)

if __name__ == '__main__':

    N, K = map(int, input().split())
    MAX = 100001
    arr = [0] * MAX
    print(bfs(N))
    print(arr)
