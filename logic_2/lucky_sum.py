# Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.
# 
# 
# lucky_sum(1, 2, 3) → 6
# lucky_sum(1, 2, 13) → 3
# lucky_sum(1, 13, 3) → 1
def lucky_sum(a, b, c):
    total = a, b, c
    new_list = []
    for i in total:
        if i == 13:
            break
        else:
            new_list.append(i)
    return sum(new_list)


print(lucky_sum(13, 2, 3))
print(lucky_sum(13, 2, 13) == 0)
print(lucky_sum(13, 13, 2) == 0)
