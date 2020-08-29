#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    
    decimal_num = 0
    digits = digits[::-1] #copy the list, slice it, reverse string
    for i in range(len(digits)):
        digit = digits[i] #individual digit at index i
        if digit.isalpha():
            digit = int(string.ascii_lowercase.index(digits[i].lower()) + 10)
            # if digit at index is alphabetic: call the lowercase, 
            # and set decimal_num equal to 10 more than its corresponding 
            # index function in the ascii_lowercase library method of string
        else:
            digit = int(digits[i])
            # else: set decimal_num to corresponding integer value
        decimal_num += (digit * base ** i) 
        #multiply digit by base to the power of the index
    return decimal_num
    
print (decode("A56", 16)) # we want 2646


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # TODO: Encode number in binary (base 2)
            
    encoded_number = ""
    division_result = number
    while division_result > base:
        division_result = division_result // base #double division gives integer answers not floats, and removes remainder
        remainder = division_result % base #gets remainder
        if base == 16:
            #convert
            encoded_number += remainder
        
        
        elif base == 2:
            pass
            #convert
            
        elif base == 10:
            pass
            #convert
        
    #very end left with a string of remainders
    #reverse string
    #TODO how do we take those string digits and convert them into correct form?
    
    
    # number = number[::-1]
    # for i in range(len(number)):
    #     numbers = numbers[i]
    #     number = int(number, base)
    #     base_num += number * base ** i
        
    #     number * base ** i
        
    #     8 = 1000(2)
    #     8//2 = 4 : 0
    #     4//2 = 2 : 0
    #     2//2 = 1 : 0
        
    #     ans = ""
    #     ans = rem + ans #adds answer to front of list
        
        
    # while digits >= base:
    #     quotient = digits // base
    #     rem = digits % base
    #     ans = str(rem) + ans
    #     if digits >= base:
    #         digits = quotient
    #     else: 
    #         ans = str(digits) + ans
    #         break
        
    
    # return str(ans)
    # TODO: Encode number in hexadecimal (base 16)
    # ...
    # TODO: Encode number in any base (2 up to 36)
    # ...
print(encode(9, 2)) # we want 1001

def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...
    #convert base 1 to base 2
    # we have functions that convert base 1 to base 10
    # ad base 10 -> base 2
    base10 = decode(digits, base1)
    result = encode(base10, base2)
    return result
    


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()