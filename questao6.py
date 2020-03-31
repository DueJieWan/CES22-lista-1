import numpy as np

def is_prime(n):
    if n == 2:
        return True
    for i in range(int(np.sqrt(n))):
        if not n % (i + 2):
          return False
    return True


print(is_prime(11))
print(not is_prime(35))
print(is_prime(19911121))
print(is_prime(2))