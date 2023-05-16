# 
# Return the number of times that the string "hi" appears anywhere in the given string.
# 
# 
# count_hi('abc hi ho') → 1
# count_hi('ABChi hi') → 2
# count_hi('hihi') → 2

def count_hi(str):
    str_strip = str.strip()
    count = 0
    if len(str_strip) < 2:
        return 0
    for i in range(len(str_strip) - 1):
        if str_strip[i: i + 2] == 'hi':
            count += 1
            i += 2
    return count


print(count_hi('hihi'))
