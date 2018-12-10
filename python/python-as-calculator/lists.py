# List are comma separated values enclosed in square brackets

squares = [1, 4, 5, 6, 9, 15]
print(squares)

# Just like strings, arrays can be indexed using numbers
print('Find third item in list using number 2 => {0}'.format(squares[2]))
# 5

print('Find last item in list using index -1 => {0}'.format(squares[-1]))
# 15

print('Find items from third last index to the end -> {0}'.format(squares[-3:]))
# [6, 9, 15]

# Cloning
newSquares = squares[:]
print('new Squares => {0}'.format(newSquares))

newSquares[0] = 123
print('New squares => {0}'.format(newSquares))
# [123, 4, 5, 6, 9, 15]

print('Squares => {0}'.format(squares))
# [1, 4, 5, 6, 9, 15]

