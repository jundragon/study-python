import unittest
import math
import random

if __name__ == '__main__':
    unittest.main()


# 다른 진법 수 -> 10진수
def convert_to_decimal(number, base):
    multiplier = 1
    result = 0
    while number > 0:
        result += number % 10 * multiplier
        multiplier *= base
        number = number // 10

    return result


# 10진수 -> 다른 진법 수
def convert_from_decimal(number, base):
    pass


# 10진수 -> 20이하 진법 수
def convert_from_decimal_larger_bases(number, base):
    pass


# 재귀 함수를 사용한 진법 변환
def convert_dec_to_any_base_rec(number, base):
    pass


# 최대공약수 찾기
def finding_gcd(number1, number2):
    pass


# 재귀 호출 사용
def find_fibonacci_seq_rec(n):
    pass


# 반복문 사용
def find_fibonacci_seq_iter(n):
    pass


# 수학 수식 사용
def find_fibonacci_seq_form(n):
    pass


# 제너레이터 사용
def find_fibonacci_seq_generator(n):
    pass


def finding_prime(number):
    pass


def finding_prime_sqrt(number):
    pass


def finding_prime_fermat(number):
    pass


class TestingNumbers(unittest.TestCase):
    # 진법 변환
    def test_convert_to_decimal(self):
        number, base = 1001, 2
        assert (convert_to_decimal(number, base) == 9)
        print("다른 진법 -> 10진수 변환 테스트 통과!")

    def test_convert_from_decimal(self):
        number, base = 9, 2
        assert(convert_from_decimal(number, base) == 1001)
        print("10진수 -> 다른 진법 변환 테스트 통과!")

    def test_convert_from_decimal_larger_bases(self):
        number, base = 31, 16
        assert(convert_from_decimal_larger_bases(number, base) == "1F")
        print("테스트 통과")

    def test_convert_dec_to_any_base_rec(self):
        number, base = 9, 2
        assert(convert_dec_to_any_base_rec(number, base) == "1001")
        print("테스트 통과")

    # 최대공약수
    def test_finding_gcd(self):
        number1, number2 = 21, 12
        assert(finding_gcd(number1, number2) == 3)
        print("최대공약수 테스트 통과!")

    # 피보나치 수열
    def test_find_fib(self):
        n = 10
        assert(find_fibonacci_seq_rec(n) == 55)
        assert(find_fibonacci_seq_iter(n) == 55)
        assert(find_fibonacci_seq_form(n) == 55)
        assert(find_fibonacci_seq_generator(n) == 55)
        print("피보나치 수열 테스트 통과!")

    # 소수
    def test_finding_prime(self):
        number1, number2 = 17, 20
        assert(finding_prime(number1) is True)
        assert(finding_prime(number2) is False)
        assert(finding_prime_sqrt(number1) is True)
        assert(finding_prime_sqrt(number1) is False)
        assert(finding_prime_fermat(number1) is True)
        assert(finding_prime(number1) is False)

        print("소수 테스트 통과!")
