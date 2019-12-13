# method 1, use list method to reverse the string
def reverse_int_str1(x):
    if x <= (2**31)-1 and x >= -2**31:
                
        if x >= 0:
            a = list(str(x))
            a.reverse()
            result = int(''.join(a))
        else:
            a = list(str(abs(x)))
            a.reverse()
            result = -1*int(''.join(a))
    else:
        result = 0

    if result <= (2**31)-1 and result >= -2**31:
        return result
    else:
        return 0


# method 2, use slicing to reverse the string
def reverse_int_str2(x):
    if x <= (2**31)-1 and x >= -2**31:

        if x >= 0:
            a = str(x)
            result = int(a[::-1])
        else:
            a = str(-x)
            result = -int(a[::-1])

    else:
        result = 0

    if result <= (2**31)-1 and result >= -2**31:
        return result
    else:
        return 0

print(reverse_int_str1(-12345))
print(reverse_int_str2(-12345))