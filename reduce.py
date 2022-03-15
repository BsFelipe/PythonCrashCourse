# reduce() = apply a function to an iterable and reduce it to a single comulative value
#            performs function on first two elements and repeats process until 1 value remains

import functools

#letters = ["F", "E", "L", "I", "P", "E"]
#word = functools.reduce(lambda x, y: x + y, letters)
#print(word)

factorial = [5, 4, 3, 2, 1]
result = functools.reduce(lambda x, y, : x * y, factorial)
print(result)
