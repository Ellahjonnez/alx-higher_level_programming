#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    # Allocating value to a and b
    a = 10
    b = 5

    # Addition
    add_result = add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, add_result), end='\n')

    #Subtraction
    sub_result = sub(a, b)
    print("{:d} - {:d} = {:d}".format(a, b, sub_result), end='\n')

    # Multiplication
    mult_result = mul(a, b)
    print("{:d} * {:d} = {:d}".format(a, b, mult_result), end='\n')

    # Divsion
    div_result = div(a, b)
    print("{:d} / {:d} = {:d}".format(a, b, div_result), end='\n')
