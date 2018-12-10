

def string_test():

    # strings can be enclosed in single quotation or double quotation

    # Escaping
    print('Hi  This is paige\'s blog')

    # Strings can be glued together with +
    print(3*'paige' + 'hi')

    # \n means new line
    print('first line \n second line')

    # put r in front of string and \ is interpreted as special character
    print(r'first line \n second line')

    print('this is a a very long text'
          'You can just write list this with no +')

    # Strings can be indexed just like arrays
    word = 'Hello'
    print(word[0])
    # H

    # Last character
    print(word[-1])
    # o

    # Second last character
    print(word[-2])
    # l

    # slicing is supported
    # Characters from position 0 (included) to position 2 (not included)
    print(word[0:2])
    # He

    # Start is always included and end always excluded
    print(word[:2] + word[2:])
    # Hello

    print(word[:2])
    # He

    print(word[4:])
    # o

    print(word[-2:])
    # lo

    # Strings in python cannot be changed. They're like const in javascript
    # word[0] = 'J'
    # This is an error

    # Create a different string if you need a new one
    anotherword = 'Y' + word[1:] + 'w'
    print(anotherword)

    # To find the length of a string use len
    print(len(word))


def main():
    string_test()


if __name__ == '__main__':
    main()