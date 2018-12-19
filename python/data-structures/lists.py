def listmethods():

    list = [1, 2, 3, 4, 5]

    # .append
    list.append(6)
    print(list)
    # [1,2,3,4,5,6]

    # ------------------------------------

    # .extend
    list.extend([3, 4, 5])
    print(list)
    # [1, 2, 3, 4, 5, 6, 3, 4, 5]

    # ------------------------------------

    # difference between extend and append
    list.append([3, 4, 5])
    print(list)
    # [1, 2, 3, 4, 5, 6, 3, 4, 5,[3,4,5]]s

    # ------------------------------------

    # .insert
    a = [1, 2, 3, 4, 5]
    a.insert(0, 100)
    print(a)
    # [100,1,2,3,4,5]

    # ------------------------------------

    # .remove
    a.remove(2)
    print(a)
    # [100, 1, 3, 4, 5]



def main():
    listmethods()


if __name__ == '__main__':
    main()

