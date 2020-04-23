# import sys
#
# sys.stdin = open('../result/input.txt', 'r')
# sys.stdout = open('../result/output.txt', 'w')

if __name__ == '__main__':
    move = ['go','go','right','go','right','go','left','go']
    r, c = 1, 0
    office = [[5, -1, 4], [6, 3, -1], [2, -1, 1]]
    answer = 0
    N = len(office)
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)] # UP: 0 RIGHT: 1, DOWN: 2, LEFT: 3
    state = 0 # 초기 상태 북쪽(UP)

    # 현재 있는 위치를 청소한다
    answer += office[r][c]
    office[r][c] = 0

    for order in move:
        # 이동 명령에 따른 좌표를 계산한다
        if order == "go":
            # 현재 방향으로 이동하고 청소한다
            y = r + d[state][0]
            x = c + d[state][1]
            if x < 0 or y < 0 or x >= N or y >= N:
                # 이동할 수 없는 구역 (이동 불가)
                continue
            if office[y][x] == -1:
                # 장애물이 있는 구역 (이동 불가)
                continue
            # 청소
            r, c = y, x
            answer += office[r][c]
            office[r][c] = 0
        elif order == "right":
            # 방향을 설정 (시계방향 +)
            state = (state+1) % 4
        elif order == "left":
            # 방향을 설정 (반시계방향 -)
            state = (state-1) % 4

    print(answer)