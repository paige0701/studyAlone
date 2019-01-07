def sets():
    # Sets : Curly braces can be used or set() function is used to make sets
    fruits = {'apple', 'mango', 'apple', 'mango'}  # duplicates are removed
    print(fruits)  # {'apple', 'mango'}

    print('mango' in fruits)  # True

    a = set('Banana')
    b = set('Bananas in pajamas')
    print(a)  # {'n', 'a', 'B'}  - unique letters in a
    print(b)  # {'m', 'n', 'j', 'B', 'i', ' ', 'a', 'p', 's'} - unique letters in b
    print(a - b)  # set() - letters in a but not in b
    print(b - a)  # {' ', 'j', 'p', 'i', 's', 'm'} - letters in b but not in a
    print(a | b)  # {'m', 'B', ' ', 'i', 'p', 'a', 'n', 's', 'j'} - letters in a and b
    print(a & b)  # {'B', 'a', 'n'} - letters in a and b
    print(a ^ b)  # {'j', 'p', 'i', ' ', 's', 'm'} - letters in a or b but not in both

    a = {x for x in 'abracadabra' if x not in 'abc'}
    print(a)  # {'d', 'r'}



def main():
    sets()


if __name__ == '__main__':
    main()