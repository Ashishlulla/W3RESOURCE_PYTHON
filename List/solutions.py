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
