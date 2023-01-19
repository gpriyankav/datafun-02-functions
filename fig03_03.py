# fig03_03.py
"""Using nested control statements to analyze examination results."""

# initialize variables
passes = 0  # number of passes
failures = 0  # number of failures

# process 10 students
for student in range(10):
    # get one exam result
  """   
    result = 0
    while result != 1 and result !=2: #it goes on to the loop until user enter sufficient 1's and 2's s
  """      
result = int(input('Enter result (1=pass, 2=fail): '))

if result == 1:
        passes = passes + 1
else:
        failures = failures + 1

# termination phase
print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
    print('Bonus to instructor')
