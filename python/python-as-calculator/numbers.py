# Using python as a calculator

# Numbers operators - + * / work same as other languages


def number_arithmetic_test():

    # classic division returns a float
    print(17/3)
    # 5.66666666

    # floor division discards the fractional part
    print(17//3)
    # 5

    # the % operator returns the remainder of the division
    print(17 % 3)
    # 2

    # squared
    print(5**2)
    # 25

    # multiplication
    print(1*2)

    # subtraction
    print(10-8)

    # addition
    print(12+3)


def main():
    number_arithmetic_test()


if __name__ == "__main__":
    main()
