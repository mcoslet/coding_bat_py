# 
# Given an int array length 2, return True if it contains a 2 or a 3.
# 
# 
# has23([2, 5]) → True
# has23([4, 3]) → True
# has23([4, 5]) → False

def has23(arr):
    return arr[0] == 2 or arr[0] == 3 or arr[1] == 2 or arr[1] == 3


print(has23([4, 3]))
print(has23([4, 5]))