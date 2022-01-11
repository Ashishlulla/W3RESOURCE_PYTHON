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

# 4. Write a Python program to sort a list of dictionaries using Lambda.
# Original list of dictionaries :

# [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
#  {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
#  {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# Sorting the List of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
#  {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
#  {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]

a = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
     {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
     {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

a_sorted = sorted(a, key=lambda x: x["color"])
print(a_sorted)

# 5. Write a Python program to filter a list of integers using Lambda.
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Even numbers from the said list:
# [2, 4, 6, 8, 10]
# Odd numbers from the said list:
# [1, 3, 5, 7, 9]

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filter_even = list(filter(lambda x: x % 2==0, a))
filter_odd = list(filter(lambda x : x % 2 == 1, a))
print(filter_even, "\n", filter_odd)
#
# 6.Write a Python program to square and cube every number in a given list of integers using Lambda. Go to the editor
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Square every number of the said list:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Cube every number of the said list:
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square = list(map(lambda x: x**2, a))
cube = list(map(lambda x: x**3, a))
print(square)
print(cube)
