"""
Always start with a docstring that describes what the module does.
Include your name and the date.

Use built-in functions and 
functions from the math module.

To illustrate the ability to call functions and 
display useful results to the user. 

Use your textbook and the examples in this repo to get ideas.

"""

# Priyanka Gorentla Date- 1/19/2023

import math
import statistics


# define some functions

def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?

    """

    # Use a try / except / finally block when something 
    # could go wrong
    try: 
        area = length * width
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# define more functions here (see instuctions)

#Calculating total number of students by doing sum of all students who joined seperatly (different intervals of time)

def total_no_of_yoga_stud(*students):
 return math.fsum(students)

#calculation average strength of the yoga class

def avg_stu_yogaclass(*students):
    return statistics.mean(students)

#another way to calculate average     

def avg_stud_yogaclass(*studs):
    return sum(studs)/len(studs)

#calculate total income of yoga institite 

def mont_income_yoga(studs):
    
 try:
    if studs != 0:
        return 500 * studs
 except Exception as ex:
    print(f'Error: {ex}')
    return None

        
# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("Explore some functions in the math module")
    print()
    print(f"math.comb(5,1) = {math.comb(5,1)}")
    print(f"math.perm(5,1) = {math.perm(5,1)}")
    print('\n')

#Calling get_area_of_lot(6, 2) and displaying the result. 

print("area of lot with length 6 and width 2 is:",get_area_of_lot(6,2))
print()
print("area of lot with length 6 and width 2 is:",get_area_of_lot(16,22))
print()
print("area of lot with length 6 and width 2 is:",get_area_of_lot(8,19))
print()

#calling avg_stu_yogaclass , avg_stud_yogaclass ,total_no_of_yoga_stud and mont_income_yoga functions

print(f"total number of students in Yoga class:{total_no_of_yoga_stud(1,2,3,4,5,6,7)}")
print()
print(f"average:{avg_stu_yogaclass(1,2,3,4,5,6,7)}")
print()
print(f"average:{avg_stud_yogaclass(1,2,3,4,5,6,7)}")
print()
print(f"monthly income of yoga institute:{mont_income_yoga(6)}")
print()




