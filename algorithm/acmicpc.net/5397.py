# 키로거
# https://www.acmicpc.net/problem/5397

import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')

if __name__ == '__main__':
    case = int(input())
    for _ in range(case):
        data = input()

        left = []
        right = []

        for _ in data:
            if _ == '<':
                if left:
                    w = left.pop()
                    right.append(w)
            elif _ == '>':
                if right:
                    w = right.pop()
                    left.append(w)
            elif _ == '-':
                if left:
                    left.pop()
            else:
                left.append(_)
        print("".join(left) + "".join(right[::-1]))

# if __name__ == '__main__':
#     case = int(input())
#     for _ in range(case):
#         data = input()
#
#         cursor = 0
#         output = []
#         for _ in data:
#             if _ == '<':
#                 cursor = max(cursor-1, 0)
#             elif _ == '>':
#                 cursor = min(cursor+1, len(output))
#             elif _ == '-':
#                 if output:
#                     del output[cursor-1]
#                 cursor = max(cursor-1, 0)
#             else:
#                 output.insert(cursor, _)
#                 cursor += 1
#         print("".join(output))
