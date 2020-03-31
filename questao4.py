def strange_sum(list):
    sum = 0
    for x in list:
        if x % 2:
            sum = sum + x
        else:
            return sum
    return sum


list = [1, 3, 2]
print(strange_sum(list))