# Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
# 
# 
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(arr):
    return len(list(filter(lambda elem: elem % 2 == 0, arr)))


print(count_evens([2, 1, 2, 3, 4]))