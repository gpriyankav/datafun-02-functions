"""
Optional bonus. See course site for details.



>>> add_two(1,2)
3

>>> add_two("hello"," world")
'hello world'

>>> add_triangle_list( [3,4,5] )
12

>>> add_any(1,1,1,1,1,1,1,1)
8

>>> add_any_with_keywords(a=1,b=2)
3

>>> convert_ctof(0)
32.0

>>> convert_ctof(100)
212.0
"""

import doctest

# define some existing functions
def add_two(first, second):
    """Return the sum of any two arguments."""
    sum = first + second  # fix this line
    return sum

print(f"Sum of 2 numbers: {add_two(1,2)}")    
print("Addind 2 words:", (add_two("Vijay","Priyanka")))
print("Addind 2 words:", (add_two("hello","world")))
print()


def add_triangle_list(list_triangle):
    """Return the sum of three numbers in a list."""
    sum = 0
    for value in list_triangle:
        sum += value  # fix this line to add the value instead of 0
    return sum

print(f"sum of three numbers: {add_triangle_list([3,4,5])}")
print()


def add_any(*args):
    """Return the sum of numbers, using built-in *args."""
    sum = 0
    for x in args:
        sum += x  # fix this line to add x instead of 1
    return sum

print(f"Sum of numbers using args: {add_any(1,1,1,1,1,1,1,1)}")
print()

def add_any_with_keywords(**kwargs):
    """Return the sum of numbers, using built-in keyword args, **kwargs."""
    sum = 0
    for value in kwargs.values():  # use values() - name doesn't matter
        sum += value  # Use the popular and concise version of sum = sum + x
    return sum

print(f"Sum of Numbers: {add_any_with_keywords(a=1,b=2)}")
print()


# TODO: implment a new function to convert celsius to fahrenheit
# Use round as needed to make the test pass
# The name of the function is provided in the docstring above

def convert_ctof(celtemp):
    fahtemp = round(((celtemp*1.8)+32),2)
    return fahtemp
 
print(f"Celsius to Fahrenheit conversion: {convert_ctof(0)}")
print(f"Celsius to Fahrenheit conversion: {convert_ctof(100)}")


if __name__ == "__main__":


    print("===========================================================")
    print("Running doctest.testmod() function to unit test our code")
    print("===========================================================")
    print()
    doctest.testmod()
    print()
   
