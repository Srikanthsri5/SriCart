from functools import reduce
li = [1, 2, 3, 4, 5, 6]
n = reduce(lambda x, y: x * y, li)

print(n)
