# 1. Write a Python function to find the Max of three numbers.
# Solution:
def my_max(a, b, c):
    if a > b > c:
        return a
    elif b > c > a:
        return b
    else:
        return c
print(my_max(21, 12, 22))
# 2. Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

def my_sum(lst):
    add = 0
    for i in lst:
        add += i
    return add

print(my_sum([1,2,3,4,5]))

# 3. Write a Python function to multiply all the numbers in a list. Go to the editor
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336
def my_prod(lst):
    mul = 1
    for i in lst:
        mul *= i
    return mul
print(my_prod([1, 2, 3, 4, 5]))


# 4. Write a Python program to reverse a string. Go to the editor
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

def my_reverse(string):
    return string[::-1]


# 5. Write a Python function to calculate the factorial of a number.
# The function accepts the number as an argument.

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(5))
