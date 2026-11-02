"""Functions"""

# A function is a block of code which only runs when it is called. 
# Call that function as many times as you want with new input parameters inside your code later!

# TODO: Make a function that takes two numbers as input and returns the sum of those numbers.

def add_numbers(a, b):
    c = a + b
    return c

x = add_numbers(5, 9)
y = add_numbers(10, 15)
z = add_numbers(20, 30)

result = print (x, y, z)

print(sum([x, y, z]))
# TODO: Call the function with 2 and 3 and print the result.