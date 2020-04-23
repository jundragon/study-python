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
    numbers = [3, 7, 2, 8, 6, 4, 5, 1]
    k = 3
    ref_idx = 0
    cnt = 0
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if abs(numbers[j]-numbers[j-1]) > k:
                ref_idx = j
                for k in range(j, len(numbers)):
                    pass
