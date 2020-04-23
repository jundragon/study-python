from fractions import Fraction


def rounding_floats(number1, number2):
    pass


def float_to_fractions(number1):
    pass


def get_denominator(number1, number2):
    pass


def get_numerator(number1, number2):
    pass


def test_testing_floats():
    number1 = 1,25
    number2 = 1
    number3 = -1
    number4 = 5/4
    number5 = 6

    assert(rounding_floats(number1, number2) == 1.2)
    assert(rounding_floats(number1*10, number3) == 10)
    assert(float_to_fractions(number1) == number4)
    assert(get_denominator(number2, number5) == number5)
    assert(get_numerator(number2, number5) == number2)

    print("fraction 모듈 테스트 통과!")


if __name__ == '__main__':
    test_testing_floats()
