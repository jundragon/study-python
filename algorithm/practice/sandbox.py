import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')


if __name__ == '__main__':
    for n in (1, 2, 3, 4):
        print(n)