# 공유기 설치
# https://www.acmicpc.net/problem/2110
import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')

if __name__ == '__main__':
    N, C = map(int, input().split())

    home = []
    for _ in range(N):
        data = int(input())
        home.append(data)

    home.sort()
    start = abs(home[1] - home[0]) # min
    end = abs(home[-1] - home[0]) # max

    result = 0
    while start <= end:
        gap = (end + start) // 2

        # 공유기를 놓아 본다
        cnt = 1
        val = home[0]
        for idx in range(1, len(home)):
            if home[idx] >= val + gap:
                val = home[idx]
                cnt += 1
        if cnt >= C:
            result = gap
            start = gap+1
        elif cnt < C:
            end = gap-1
        else:
            start = gap+1

    print(result)


