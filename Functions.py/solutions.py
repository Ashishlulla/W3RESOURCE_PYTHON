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

# 6. Write a Python function to check whether a number falls in a given range.


def is_in_range(strt, end, num):
    if strt <= num <= end:
        return f"Number Falls in a given range"
    else:
        return f"Number Falls in a given range"


# 7. Write a Python function that accepts a string and calculate the number of upper
# case letters and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def count_lower_upper(string):
    upper_count = 0
    lower_count = 0
    for i in string:
        if i.isupper():
            upper_count += 1
        elif i.islower():
            lower_count += 1
        else:
            pass
    return f"No. of Upper case characters :{upper_count}\n" \
           f"No. of Lower case Characters : {lower_count}"


print(count_lower_upper('The quick Brow Fox'))


# 8. Write a Python function that takes a list and returns a new list with unique elements
# of the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
def unique_list(lst):
    unique = []
    for i in lst:
        if i not in unique:
            unique.append(i)
        else:
            pass
    return unique


print(unique_list([1, 2, 3, 3, 3, 3, 4, 5]))


# 9. Write a Python function that takes a number as a parameter and
# check the number is prime or
# not.
# Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive
# divisors other than 1 and itself.
def is_prime(num):
    factors = []
    for i in range(2, num):
        if num % i == 0:
            factors.append(i)
        else:
            pass
    if len(factors) > 0:
        return False
    else:
        return True

print(is_prime(12))

# 10. Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]

def even(lst):
    return [i for i in lst if i % 2 == 0]


print(even([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# 11.Write a Python function that checks whether a passed string is palindrome or not.
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward,
# e.g., madam or nurses run.

def is_palindrome(name):
    if name == name[::-1]:
        return True
    else:
        return False


print(is_palindrome("madam"))


# 12.Write a Python function to check whether a string is a pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "asdfghjklqwertyuiopzxcvbnm"

def is_pangrams(string):
    a = []
    for i in string:
        if i not in a and i != " ":
            a.append(i)
        else:
            pass
    print(a)
    if len(a) == 26:
        return True
    else:
        return False


print(is_pangrams("asdfghjklqwertyuiopzxcvbnm"))

