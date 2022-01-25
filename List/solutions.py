#  Write a Python program to sum all the items in a list.

a = [1,2,3,4,5,6]
print(sum(a))
# 2. Write a Python program to multiply all the items in a list. Go to the editor
# Click me to see the sample solution
a = [1,2,3,4,5]
mul = 1
for i in a:
    mul *=i
print(mul)

# 3. Write a Python program to get the largest number from a list. Go to the editor
# Click me to see the sample solution

a = [1,2,3,4,5]
print(max(a))

# 4. Write a Python program to get the smallest number from a list. Go to the editor
# Click me to see the sample solution
a = [1,2,3,4,5]
print(min(a))

# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
# Click me to see the sample solution

a = ['abc', 'xyz', 'aba', '1221']
print([i for i in a if len(i) > 2 and i[0] == i[-1]])

# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. Go to the editor
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
# Click me to see the sample solution

a = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sorted(a, key= lambda x:x[1]))


# 7. Write a Python program to remove duplicates from a list. Go to the editor
# Click me to see the sample solution

a = [1, 2, 3, 4, 5, 6, 7, 8, 3, 2, 14, 5, 6]
print(list(set(a)))

# 8. Write a Python program to check a list is empty or not. Go to the editor
# Click me to see the sample solution

a = []
if len(a) == 0:
    print(True)
else:
    print(False)
# 9. Write a Python program to clone or copy a list. Go to the editor
# Click me to see the sample solution

a = [1, 2, 3, 4, 5, 6, 7]
b = a.copy()
print(a == b)

# 10. Write a Python program to find the list of words that are longer than n from a given list of words. Go to the editor
# Click me to see the sample solution

a = ["Ash", 'Bhavi', 'somya']
for i in a:
    if len(i) > 3:
        print(i, end=" ")

# 11. Write a Python function that takes two lists and returns True if they have at least one common member. Go to the editor
# Click me to see the sample solution

a = [1, 2, 3, 4]
b = [4, 5, 6, 7]
for i in a:
    if i in b:
        print(True)
        break

# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Go to the editor
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']
# Click me to see the sample solution

a = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
b = [a[i] for i in range(len(a)) if i != 0 and i != 4 and i != 5]

print(b)

# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *. Go to the editor
# Click me to see the sample solution

matrix = []
for i in range(3):
    for j in range(4):
        for k in range(6):
            matrix.append([i, j, k])

print(matrix)

# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it. Go to the editor
# Click me to see the sample solution

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print([i for i in a if i % 2 != 0])
# 15. Write a Python program to shuffle and print a specified list.

import random

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(a)
print(a)
# 16. Write a Python program to generate and print a list of first and last 5 elements where the
# values are square of numbers between 1 and 30 (both included)
square = [i ** 2 for i in range(1, 31)]
print(square[:5] + square[-5:])

# 17. Write a Python program to generate and print a list except for the first 5 elements, where the values
# are square of numbers between 1 and 30 (both included).

square = [i ** 2 for i in range(1, 31)]
print(square[5:-5])

# 19. Write a Python program to get the difference between the two lists.

lst1 = [1, 2, 3, 4]
lst2 = [4, 5, 6, 7]
print(list(set(lst1).symmetric_difference(set(lst2))))

# 20. Write a Python program access the index of a list.

a = [12, 3, 2, 1, 3, 2, 5, 4, 4, 33, 2]
print([a[i] for i in range(len(a))])

# 21. Write a Python program to convert a list of characters into a string.
lst = ['a', 's', 'h', 'i', 's', 'h']
print("".join(lst))

# 22. Write a Python program to find the index of an item in a specified list.

lst = ['a', 's', 'h', 'i', 's', 'h']
print(lst.index("i"))

# 24. Write a Python program to append a list to the second list.
lst = ['a', 's', 'h', 'i', 's', 'h']
num = [1, 2, 3]
lst.append(num)
print(lst)
#
# 25. Write a Python program to select an item randomly from a list.

import random

lst = ['a', 's', 'h', 'i', 's', 'h']
print(random.choice(lst))

# 27. Write a Python program to find the second smallest number in a list.
a = [9, 8, 7, 6, 5, 5, 4, 3, 3]
a.sort()
print(a[1])

# 28. Write a Python program to find the second largest number in a list. Go to the editor
# Click me to see the sample solution

a = [9, 8, 7, 6, 5, 5, 4, 3, 3]
a.sort()
print(a[-2])

# 29. Write a Python program to get unique values from a list.

a = [1, 2, 2, 3, 4, 4, 5, 6, 7]
print([i for i in a if a.count(i) == 1])

# 30. Write a Python program to get the frequency of the elements in a list.

a = [1, 2, 2, 3, 4, 4, 5, 6, 7]
print({i: a.count(i) for i in a })
