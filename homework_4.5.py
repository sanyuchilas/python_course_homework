from functools import reduce
from math import factorial
print(reduce(lambda x, y: x * y, [num for num in range(100, 1001) if num % 2 == 0]))