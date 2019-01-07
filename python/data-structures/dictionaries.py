# Dictionaries

def dictionaries():
    tel = {'jack': 4000, 'paige': 5000}
    print(tel['jack'])  # 4000
    tel['jenny'] = 6000
    print(tel)  # {'jack': 4000, 'paige': 5000, 'jenny': 6000}
    del tel['paige']
    print(tel)  # {'jack': 4000, 'jenny': 6000}
    print(list(tel))  # ['jack', 'jenny']
    print(sorted(tel))  # ['jack', 'jenny']
    print('paige' in tel)  # False
    print('paige' not in tel)  # True
    dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])  # {'sape': 4139, 'guido': 4127, 'jack': 4098}

    print({x: x ** 2 for x in (2, 4, 6)})
    # {2: 4, 4: 16, 6: 36}

    dict(sape=4139, guido=4127, jack=4098)
    # {'sape': 4139, 'guido': 4127, 'jack': 4098}


def main():
    dictionaries()


if __name__ == '__main__':
    main()