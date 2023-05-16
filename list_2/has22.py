# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
# 
# 
# has22([1, 2, 2]) → True
# has22([1, 2, 1, 2]) → False
# has22([2, 1, 2]) → False

def has22(arr):
    if len(arr) <= 1:
        return False
    is22 = False
    for i in range(len(arr) - 1):
        if arr[i] == 2 and arr[i+1] == 2:
            is22 = True
            break
    return is22


print(has22([1, 2, 1, 2]))
print(has22([1, 2, 2]))
print(has22([2, 1, 2]))