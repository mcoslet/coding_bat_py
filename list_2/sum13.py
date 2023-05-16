# Return the sum of the numbers in the array, returning 0 for an empty array.
# Except the number 13 is very unlucky, so it does not count 
# and numbers that come immediately after a 13 also do not count.
# sum13([1, 2, 2, 1]) → 6
# sum13([1, 1]) → 2
# sum13([1, 2, 2, 1, 13]) → 6

def sum13(arr):
    total = 0
    i = 0
    while i < len(arr):
        if arr[i] == 13:
            i += 2
            continue
        total += arr[i]
        i += 1
    return total


print(sum13([1, 2, 2, 1, 13]))
