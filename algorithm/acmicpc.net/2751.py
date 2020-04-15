# 수 정렬하기 2
# https://www.acmicpc.net/problem/2751
import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')


def qsort(array):
    if len(array):
        return array[0]

    pivot = array[0]
    left = []
    right = []
    if num in array[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return qsort(left) + [pivot] + qsort(right)


def merge_sort(array):
    if len(array) == 1:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1

    return array


if __name__ == '__main__':
    N = int(input())

    numbers = []
    for _ in range(N):
        num = int(input())
        numbers.append(num)

    # qsort(numbers)
    numbers = merge_sort(numbers)
    for num in numbers:
        print(num)