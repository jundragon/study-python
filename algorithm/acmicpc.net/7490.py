# 0 만들기
# https://www.acmicpc.net/problem/7490
import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')

def make_zero(array, n):
    if len(array) == n:
        operators.append(array[:])
        return

    array.append(' ')
    make_zero(array, n)
    array.pop()

    array.append('+')
    make_zero(array, n)
    array.pop()

    array.append('-')
    make_zero(array, n)
    array.pop()

if __name__ == '__main__':
    case = int(input())

    for _ in range(case):
        n = int(input())
        operators = []

        make_zero([], n-1)

        integers = [i for i in range(1, n+1)]

        for operator in operators:
            string = ""
            for i in range(n-1):
                string += str(integers[i]) + operator[i]
            string += str(integers[-1])
            if eval(string.replace(" ", "")) == 0:
                print(string)
