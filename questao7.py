import numpy as np

def sum_of_squares(xs):
    return sum(np.square(xs))

xs = [2, 3, 4]
print(sum_of_squares(xs))