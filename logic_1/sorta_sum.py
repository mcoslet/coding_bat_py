# 
# Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.
# 
# 
# sorta_sum(3, 4) → 7
# sorta_sum(9, 4) → 20
# sorta_sum(10, 11) → 21

def sorta_sum(a,b):
    total = a+b
    if 10 <= total <= 19:
        return 20
    return total


print(sorta_sum(9, 4))