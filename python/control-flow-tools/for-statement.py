

words = ['abc', 'def', 'ghi']

for word in words:
    print(word)

print('-----------------')

# loops through 0 to 3 (not included)
for x in range(0, 3):
    print(x)

print('-----------------')

# loops through 1 to 10(not included) and number goes up by 2 so
# range(1,10,2) is [1,3,5,7,9] (having a different increment - third argument)
for x in range(1, 10, 2):
    print(x)

# if you need index when iterating combine range() and len()

for i in range(len(words)):
    print('index --> {0}'.format(i))
    print('print item with index --> {0}'.format(words[i]))


print('-----------------')


# break statements
A_list = [1, 2, 3, 4, 5]
for i in A_list:
    if i == 1:
        break
    else:
        print('else {0}'.format(i))

# since first value in the array is 1, this for loop will not print anything on the screen
# It will break out of for loop when break keyword is met in the first condition is i == 1 ?

print('-----------------')


# continue statement
for i in A_list:
    if i == 1:
        continue
    else:
        print('else {0}'.format(i))

# Continue is a bit different to break.
# Continues to the next iteration.


# pass statement - commonly used for creating minimal classes
class MyEmptyClass:
    pass


# Defining functions
def greetings():
    print('Good afternoon')


def multiple_parameters(name, age):
    print('Hi my name is {0} and I\'m {1} years old'.format(name, age))


def default_parameters(gender, name='Paige', age=15):
    print(gender)
    print(name)
    print(age)


if __name__ == '__main__':
    greetings()
    multiple_parameters('Paige', 15)
    default_parameters('Female', age=25)
