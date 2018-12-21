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

    # ------------------------------------

    # .pop
    b = [1, 2, 3, 4, 5]
    b.pop()
    print(b)
    # deletes last element in the list

    b.pop(0)
    print(b)
    # delete item at the given position in the list. in this case 0 -> 1st item in the list

    # ------------------------------------

    # .clear() removes all items in the list
    c = [1, 2, 3, 4]
    c.clear()
    print(c)

    c = [2, 3, 4]
    del c[:]
    print(c)
    # this is same as .clear()

    # ------------------------------------

    # .index(x) finds the position of x in the list
    d = [1, 2, 3, 4]
    print(d.index(1))  # returns 0

    d = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5]
    print(d.index(1, 4))  # returns 6 - find index of 1 after position 4

    d = [1, 2, 5, 6, 1, 2, 3, 4, 5, 1, 2, 1]
    # returns 0 - looks for 1 in list position 0 ~ 5 - there's two ones but returns first found index
    print(d.index(1, 0, 5))

    # ------------------------------------
    # .count(x) - counts number of x is in the list
    print(d.count(1))  # returns 4

    # ------------------------------------
    # .sort(key=None, reverse = false) - key 부분은 더 공부해야겠다.. 잘 모르겠음
    e = ['apple', 'jam', 'air', 'zebra']
    e.sort()  # ['air', 'apple', 'jam', 'zebra']
    e.sort(reverse=True)  # ['zebra', 'jam', 'apple', 'air']
    e.reverse()  # is same ase e.sort(reverse = True)
    print(e)

    # ------------------------------------
    # list.copy() - Returns shallow copy of the list same as a[:]
    f = [1, 2, 3, 4]
    g = f.copy()
    print(g)
    f[2] = 100
    print(g)  # [1, 2, 3, 4]
    print(f)  # [1, 2, 100, 4]


def main():
    listmethods()


if __name__ == '__main__':
    main()

