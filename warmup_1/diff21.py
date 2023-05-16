# Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.


def diff21(n):
    diff = abs(n-21)
    if n > 21:
        return diff*2
    return diff


print(diff21(19))
print(diff21(10))
print(diff21(21))