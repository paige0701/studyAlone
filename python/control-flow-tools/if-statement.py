# elif is shorted version of else if
# white space is extremely important in python
# no brackets when using if statement


def if_test():
    x = int(input("Please enter an integer: "))
    if x < 10:
        print("Less than 10")
    elif x < 0:
        print("Less than 0")
    else:
        print("Bigger than 10")


def main():
    if_test()


if __name__ == '__main__':
    main()

