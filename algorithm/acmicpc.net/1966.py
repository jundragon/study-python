# 프린터 큐
# https://www.acmicpc.net/problem/1966
import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')


if __name__ == '__main__':
    case = int(input())

    for _ in range(case):
        N, M = map(int, input().split())
        docs = list(map(int, input().split()))
        idx_docs = [(value, idx) for idx, value in enumerate(docs)]
        docs.sort(reverse=True)

        cnt = 0
        while idx_docs:
            d = idx_docs.pop(0)
            if d[0] == docs[0]:
                cnt += 1
                del docs[0]
                if d[1] == M:
                    break
            else:
                idx_docs.append(d)

        print(cnt)
