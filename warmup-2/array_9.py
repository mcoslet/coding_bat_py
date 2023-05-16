# Given an array of ints, return the number of 9's in the array.
# 
# 
# array_count9([1, 2, 9]) → 1
# array_count9([1, 9, 9]) → 2
# array_count9([1, 9, 9, 3, 9]) → 3

def array_count9(arr):
    new_arr = [num for num in arr if num==9]
    return len(new_arr)


print(array_count9([1, 9, 9, 3, 9]))