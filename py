#A Narcissistic Number is a number of length n in which the sum of its digits to the power of n is equal to the original number. 
#If this seems confusing, refer to the example below.

def is_narcissistic(i):
    result = 0
    snumber = str(i)
    l = len(snumber)
    for digit in snumber:
        result += int(digit)**l
        if result > i:
            return False
    if result != i:
        return False
    return True