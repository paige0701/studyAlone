# Tuples
def tuples():
    t = 123, 455, 677
    print(t[0])  # 123
    print(t)  # (123, 456, 677)

    #  t[0] = 1  # error .. can't assign value with tuple

    empty = ()
    print(len(empty))  # 0

    singleton = 'hello',
    print(singleton)
    print(len(singleton))  # 1 if singleton - 'hello' with no comma at the end, len(singleton) is 5


def main():
    tuples()


if __name__ == '__main__':
    main()
