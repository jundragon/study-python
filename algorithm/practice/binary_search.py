import random


def binary_search(data, search):
    pass


def test_binary_search():
    data_list = random.sample(range(100), 10)
    data_list.sort()
    print(data_list)
    print(binary_search(data_list, 100))
    print(binary_search(data_list, data_list[5]))


if __name__ == '__main__':
    test_binary_search()