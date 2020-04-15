# 스택 수열
# https://www.acmicpc.net/problem/1874
import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')

if __name__ == '__main__':
    N = int(input())
    stack = list()
    output = list()
    push_num = 1
    is_available = True
    for _ in range(N):
        number = int(input())
        # push
        if not stack or stack[-1] < number:
            for i in range(push_num, number+1):
                stack.append(i)
                output.append("+")
            push_num = stack[-1]+1
        elif stack[-1] > number:
            print("NO")
            is_available = False
            break

        # pop
        if stack[-1] == number:
            stack.pop()
            output.append("-")

    if is_available:
        for _ in output:
            print(_)