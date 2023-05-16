# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
# 
# 
# array123([1, 1, 2, 3, 1]) → True
# array123([1, 1, 2, 4, 1]) → False
# array123([1, 1, 2, 1, 2, 3]) → True

def array123(arr):
    for i in range(len(arr) - 2):
        if arr[i] == 1 and arr[i+1] == 2 and arr[i+2] == 3:
            return True
    return False