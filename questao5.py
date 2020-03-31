def n_sam_repeats(list):
    count = 0
    for word in list:
        if word != "sam":
            count = count + 1
        else:
            count = count + 1
            return count
    return count


list = ["i", "am", "not", "sam"]

print(n_sam_repeats(list))