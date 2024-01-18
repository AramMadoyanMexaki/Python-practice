def array_diff(arr1, arr2):
    result_arr = []

    for i in arr1:
        if i not in arr2:
            result_arr.append(i)

    return result_arr

print(array_diff([1, 2, 3], [1, 2]))