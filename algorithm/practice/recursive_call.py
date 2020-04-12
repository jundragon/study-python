# 1부터 입력 숫자까지 곱을 재귀 호출로 구현
def multiple(data):
    if data <= 1:
        return data
    return data * multiple(data-1)

# 입력된 리스트의 합을 재귀 호출로 구현
def sum_list(data):
    if len(data) == 1:
        return data[0]
    return data[0] + sum_list(data[1:])

# 회문을 판별할 수 있는 함수
def palindrome(data):
    # 단어를 뒤집어서 비교하는 방법
    re = [c for c in data[::-1]]
    if data == "".join(re):
        return True
    else:
        return False

def palindrome_re(data):
    # 재귀 호출로 구현
    if len(data) <= 1:
        return True

    if data[0] == data[-1]:
        return palindrome_re(data[1:-1])
    else:
        return False

def practice1(data):

    if data % 2 == 1:
        data = 3 * data + 1
    else:
        data //= 2

    if data == 1:
        return data

    print(data)
    return practice1(data)

def practice2(n):

    if n == 1:
        return n

    print(n)

    if n % 2 == 1:
        return practice2(3*n+1)
    else:
        return practice2(n//2)

def practice3(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return practice3(n-1) + practice3(n-2) + practice3(n-3)

if __name__ == '__main__':
    print(multiple(10))
    print(sum_list([1, 2, 3, 4, 5]))
    print(palindrome("level"))
    print(palindrome_re("level"))

    print(palindrome("revel"))
    print(palindrome_re("revel"))

    print(practice2(3))
    print(practice3(4))
