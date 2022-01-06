# Question :
# 1.Write a Python program to calculate the length of a string.

a = "String"
print(len(a))

# 2.Write a Python program to count the number of characters (character frequency) in a string.

a = "google.com"
dict1 = {}
for i in a:
    dict1[i] = a.count(i)

print(dict1)

#  3.Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
#   If the string length is less than 2, return instead of the empty string.

a =  'w3'
if len(a) < 2:
    print("")
elif len(a) == 2:
    print(a*2)
else:
    print(a[:2]+ a[-2:])
