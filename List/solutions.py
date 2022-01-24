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
