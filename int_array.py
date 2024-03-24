def is_int_arr(arr):
    if not arr:
        return True

    for i in arr:
        if not isinstance(i, (int, float)) or i != int(i):
            return False

    return True

print(is_int_arr([1, 2, 3, 4.6]))
