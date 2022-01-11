# 1. Write a Python program to create a lambda function that adds 15 to a given number
# passed in as an argument, also create a lambda function that multiplies argument x
# with argument y and print the result.
# Solution:

add = lambda x: x + 15
mul = lambda x, y: x * y

a = int(input("Enter the Number 1st: "))
b = int(input("Enter the Number 2nd: "))
print(add(a))
print(mul(a, b))

# 2. Write a Python program to create a function that takes one argument, and that argument
# will be multiplied with an unknown given number.
# Sample Output:
# Double the number of 15 = 30
# Triple the number of 15 = 45
# Quadruple the number of 15 = 60
# Quintuple the number 15 = 75

def multiplier(n):
    a = lambda x : x * n
    return a

number = int(input("Enter the Number: "))
double = multiplier(2)
print(f"Double of {number} is {double(number)}")
triple = multiplier(3)
print(f"triple of {number} is {triple(number)}")
quadruple = multiplier(4)
print(f"quadruple of {number} is {quadruple(number)}")
quintuple = multiplier(5)
print(f"quintuple of {number} is {quintuple(number)}")


# 3. Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

a = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
a_sorted = sorted(a, key= lambda x: x[1])
print(a_sorted)
