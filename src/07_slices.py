"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 
This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295
Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]


# Output the second element: 4:
second = a[1]
print('second element:', second)

# Output the second-to-last element: 9
second_to_last = a[-2]
print('second to last element:', second_to_last)

# Output the last three elements in the array: [7, 9, 6]
last_three = a[3:]
print('last three elements:', last_three)

# Output the two middle elements in the array: [1, 7]
middle_elements = a[2:4]
print('middle elements:', middle_elements)

# Output every element except the first one: [4, 1, 7, 9, 6]
first_exempt = a[1:]
print('first element exempt:', first_exempt)

# Output every element except the last one: [2, 4, 1, 7, 9]
last_exempt = a[:-1]
print('last element exempt:', last_exempt)

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
world = s[7:12]
print('hello world output:', world)

