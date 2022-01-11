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

#  7.Write a Python program to count the even, odd numbers in a given array of integers using Lambda. Go to the editor
# Original arrays:
# [1, 2, 3, 5, 7, 8, 9, 10]
# Number of even numbers in the above array: 3
# Number of odd numbers in the above array: 5

a = [1, 2, 3, 5, 7, 8, 9, 10]
count_even = len(list(filter(lambda x: x % 2==0, a)))
count_odd = len(list(filter(lambda x: x % 2==1, a)))
print("no of even in list:", count_even)
print("no of od in list", count_odd)

# 8. Write a Python program to find the values of length six in a given list using Lambda.

a = ["Ashish", "Bhavesh", "Somesh", "Aadi", "Mitali", "Akshay", "Shruti"]
b = list(filter(lambda x : len(x) == 6, a))
print(b)

# 9.Write a Python program to add two given lists using map and lambda.
# Original list:
# [1, 2, 3]
# [4, 5, 6]
# Result: after adding two list
# [5, 7, 9]

a, b =[1, 2, 3], [4, 5, 6]
print(list(map(lambda x, y: x+y, a, b)))

# 10. Write a Python program to find the second lowest grade of any student(s)
# from the given names and grades of each student using lists and lambda.
# Input number of students, names and grades of each student.
#
student_scores = []
n = int(input("Enter the number of Student "))
for i in range(n):
    name = str(input("Enter the Name of Student: "))
    grade = float(input("Enter the grade of Student: "))
    student_scores.append([name, grade])


student_sorted = sorted(student_scores, key= lambda x: x[1])
print(f"Second Lowest Grade: {student_sorted[-2][1]}")
print(f"Name: {student_sorted[-2][0]}")

# 11.Write a Python program to find numbers divisible by nineteen or thirteen from a list
# of numbers using Lambda.
# Orginal list:
# [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
# Numbers of the above list divisible by nineteen or thirteen:
# [19, 65, 57, 39, 152, 190]

a = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
filtered = list(filter(lambda x: x % 13==0 or x % 19 == 0, a))
print(filtered)

# 12. Write a Python program to find palindromes in a given list of strings using Lambda. Go to the editor
# Orginal list of strings:
# ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
# List of palindromes:
# ['php', 'aaa']

a = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
filter_palindromes = list(filter(lambda x:x == x[::-1], a))
print(filter_palindromes)
