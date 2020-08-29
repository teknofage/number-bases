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
    # ...
    # TODO: Encode number in hexadecimal (base 16)
    # ...
    # TODO: Encode number in any base (2 up to 36)
    # ...
    # new_base_number = 0
    digits_and_letters = string.digits + string. ascii_letters
    print(digits_and_letters)
    final_digits = ""
    while number != 0:
        # print("divisor = ", number)
        remainder = number % base
        # print("remainder = ", remainder)
        number = number // base
        final_digits += str(remainder)
    # print(final_digits)
    return final_digits[::-1]
    
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
    # base10result = decode(digits, base1)
    string = decode(digits, base1)
    
    return encode(int(string), base2)
    
print(convert(9, 2, 16)) # we want 1001


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