# 음계
# https://www.acmicpc.net/problem/2920
import sys
sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')

if __name__ == '__main__':
    numbers = list(map(int, input().split()))

    asc = True
    desc = True
    for idx in range(1, len(numbers)):
        diff = numbers[idx-1] - numbers[idx]
        if diff == -1:
            desc = False
        elif diff == 1:
            asc = False
        else:
            desc = False
            asc = False
            break

    if asc:
        print("ascending")
    elif desc:
        print("descending")
    else:
        print("mixed")
