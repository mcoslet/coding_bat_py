# Return the sum of the numbers in the array, except ignore sections of numbers starting 
# with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). 
# Return 0 for no numbers.
# sum67([1, 2, 2]) → 5
# sum67([1, 2, 2, 6, 99, 99, 7]) → 5
# sum67([1, 1, 6, 7, 2]) → 4

def sum67(arr):
    total = 0
    i = 0
    while i < len(arr):
        if arr[i] == 6:
            total -= 7
            while arr[i] != 7:
                print(f'index: {i}')
                i += 1
        total += arr[i]
        i += 1
    return total


print(sum67([1, 2, 2, 6, 99, 99, 7]))
print(sum67([1, 1, 6, 7, 2]))
print(sum67([1, 2, 2]))
