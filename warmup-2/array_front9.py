# Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.
# 
# 
# array_front9([1, 2, 9, 3, 4]) → True
# array_front9([1, 2, 3, 4, 9]) → False
# array_front9([1, 2, 3, 4, 5]) → False

def array_front9(arr):
    if len(arr) >= 4:
        new_arr = [num for num in arr[:4] if num==9]
    else:
        new_arr = [num for num in arr if num==9]
    return len(new_arr) > 0


print(array_front9([1, 2, 3, 4, 5]))