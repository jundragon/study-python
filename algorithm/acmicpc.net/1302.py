# 베스트 셀러
# https://www.acmicpc.net/problem/1302
import sys

sys.stdin = open('../result/input.txt', 'r')
sys.stdout = open('../result/output.txt', 'w')

if __name__ == '__main__':
    N = int(input())

    books = dict()
    for _ in range(N):
        book = input()
        if book not in books:
            books[book] = 1
        else:
            books[book] += 1
            
    target = max(books.values())
    array = []
    for book, number in books.items():
        if number == target:
            array.append(book)
    print(sorted(array)[0])
