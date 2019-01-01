def listmethods():

    list1 = [1, 2, 3, 4, 5]

    # .append
    list1.append(6)
    print(list1)
    # [1,2,3,4,5,6]

    # ------------------------------------

    # .extend
    list1.extend([3, 4, 5])
    print(list1)
    # [1, 2, 3, 4, 5, 6, 3, 4, 5]

    # ------------------------------------

    # difference between extend and append
    list1.append([3, 4, 5])
    print(list1)
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

    # ------------------------------------
    # Using list as deque
    from collections import deque
    queue = deque(["Eric", "John", "Steve"])
    queue.append("Jenny")
    print(queue)
    queue.popleft()
    print(queue)

    # ------------------------------------
    squares = []
    # for x in range(10):
    #     squares.append(x**2)
    #
    # print(squares)

    # this statement is same as the one before
    squares = [x ** 2 for x in range(10)]
    print(squares)

    squares = [-2, 0, 2, 4, 6, 8]

    # create a new list with the values doubled
    # squares = [x*2 for x in squares]

    # filter the list to exclude negative numbers
    # squares = [x for x in squares if x >= 0]

    # apply a function to all the elements
    squares = [abs(x) for x in squares]
    print(squares)

    freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
    freshfruit = [weapon.strip() for weapon in freshfruit]  # .strip() is like .trim() in javascript
    print(freshfruit)

    # create a list of 2-tuples like (number, square)
    # [x, x**2 for x in range(6)] tuple mush be parenthesized ! like (x, x**2)
    yy = [(x, x**2) for x in range(6)]
    print(yy)  # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

    # flatten a list using a listcomp with two 'for'
    vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    vec = [num for elem in vec for num in elem]
    print(vec)

    # ------------------------------------
    # Nested List Comprehensions
    matrix = [
         [1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
     ]

    # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

    # matrix = [[row[x] for row in matrix] for x in range(4)]

    list(zip(*matrix))

    print(list(zip(*matrix)))

    # ------------------------------------
    # Tuples
    t = 123, 455, 677
    print(t[0])  # 123
    print(t)  # (123, 456, 677)

    #  t[0] = 1  # error .. can't assign value with tuple

    empty = ()
    print(len(empty))  # 0

    singleton = 'hello',
    print(singleton)
    print(len(singleton))  # 1 if singleton - 'hello' with no comma at the end, len(singleton) is 5

    # ------------------------------------
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
    listmethods()


if __name__ == '__main__':
    main()

