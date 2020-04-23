# 중량제한
# https://www.acmicpc.net/problem/1939
import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')


from collections import deque

# 경로가 있는지 탐색하는 알고리즘
def bfs(c):
    queue = deque([start_node])
    visited = [False] * (n+1)
    visited[start_node] = True
    while queue:
        x = queue.popleft()
        for y, weight in adj[x]:
            if not visited[y] and weight >= c:
                visited[y] = True
                queue.append(y)
    return visited[end_node]

if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n+1)]

    start = 1000000000
    end = 1

    for _ in range(m):
        x, y, weight = map(int, input().split())
        adj[x].append((y, weight))
        adj[y].append((x, weight))
        start = min(start, weight) # min
        end = max(end, weight) # max

    start_node, end_node = map(int, input().split())

    result = start
    while start <= end:
        mid = (start + end) // 2
        if bfs(mid):
            result = mid
            start = mid + 1
        else:
            end = mid-1

    print(result)
