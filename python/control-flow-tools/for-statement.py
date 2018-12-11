

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



