def move_zeros(array):
    non_zeros = []
    zeros = []
    new_arr = []

    for i in array:
        if i != 0:
            non_zeros.append(i)
        else:
            zeros.append(i)

    new_arr = non_zeros + zeros

    return new_arr



print(move_zeros([1, 0, 3, 5, 10, 0, 4, 7, 9, 3, 6, 2, 0, 4, 3]))
