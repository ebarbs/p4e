# Finding Numbers in a Haystack
#
# In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in
# the file and compute the sum of the numbers.
#
# Data Files
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the
#  other is the actual data you need to process for the assignment.
#
# Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
# Actual data: http://py4e-data.dr-chuck.net/regex_sum_43683.txt (There are 79 values and the sum ends with 321)
# These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python
# program. Note: Each student will have a distinct data file for the assignment - so only use your own data file for
# analysis.
# Data Format

import re

name = input("Enter file:")
if len(name) < 1 : name = "regex_sum_43683.txt"
handle = open(name)

num_sum = 0

for line in handle:
    y = re.findall("[0-9]+", line)
    for x in y:
        if not x == None:
            tmp = int(x)
            num_sum = num_sum + tmp

print (num_sum)

