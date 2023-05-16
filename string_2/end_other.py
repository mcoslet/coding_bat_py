# Given two strings, return True if either of the strings appears at the very end of the other string,
# ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
# Note: s.lower() returns the lowercase version of a string.
# 
# 
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True

def end_other(a, b):
    a_lower = a.lower()
    b_lower = b.lower()
    if len(a_lower) == len(b_lower):
        return a_lower == b_lower
    if len(a_lower) > len(b_lower):
        return a_lower[-len(b_lower):] == b_lower
    return b_lower[-len(a_lower):] == a_lower


print(end_other('Hiabc', 'abc'))
print(end_other('abc', 'abXabc'))