#!/usr/bin/python3
def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False


def is_power(a,b):
    if a == b or b == 1 and a or b == 0:
        return True

    else:
        case1 = is_divisible(a,b)
        case2 = is_divisible(a , int(a/b))
        return is_power(case1,case2)


print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))